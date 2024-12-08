from dotenv import load_dotenv
import os

from neo4j import GraphDatabase, basic_auth
import openai

from neo4j_graphrag.retrievers import Text2CypherRetriever
from neo4j_graphrag.llm import OpenAILLM

from neo4j import GraphDatabase

from neo4j_graphrag.generation import GraphRAG

import gradio as gr

from make_schema import get_schema, format_schema
from content import lecture, structure, cypher

def ready_gpt(user_api_key):
    try:
        driver = GraphDatabase.driver(
        "bolt://184.72.178.158:7687",
        auth=basic_auth("neo4j", "formulas-method-blood"))

        llm = OpenAILLM(model_name="gpt-4o", model_params={"temperature": 0}, api_key = user_api_key)
        test_prompt = "Hello! How are you?"
        response = llm.invoke(test_prompt).content
        if response:  # LLM 연결 성공
            print(response)
            
            # Neo4j Schema 가져오기 및 포맷
            schema = get_schema("bolt://184.72.178.158:7687", "neo4j", "formulas-method-blood")
            neo4j_schema = format_schema(schema)

            # LLM INPUT / QUERY 예시
            examples = [
                """USER INPUT: '배수지가 풀었던 문제 코드와 문제 질문을 알려주세요.'
                QUERY: MATCH (p:Person {name:'배수지'})-[r:SOLVED]->(q:Question)
                RETURN q.code, q.question LIMIT 10""",

                """USER INPUT: '배수지가 아직 풀지 않은 문제 코드와 문제 질문을 확인할 수 있을까요?'
                QUERY: MATCH (p:Person {name:'배수지'})-[r:UNSOLVED]->(q:Question)
                RETURN q.code, q.question""",

                """USER INPUT: '4학년 학생들이 풀었던 질문의 평균 점수는 얼마인가요?'
                QUERY: MATCH (g:Grade {grade:'4'})<-[:belongs_to]-(p:Person)-[r:SOLVED]->(q:Question)
                RETURN AVG(r.score) AS avgScore""",

                """USER INPUT: '4학년 학생들이 가장 많이 푼 질문을 알고 싶어요.'
                QUERY: MATCH (g:Grade {grade:'4'})<-[:belongs_to]-(p:Person)-[r:SOLVED]->(q:Question)
                RETURN q.code, q.question, COUNT(r) AS solveCount
                ORDER BY solveCount DESC LIMIT 1""",

                """USER INPUT: '4학년 학생들이 가장 오랜 시간 풀었던 문제는 무엇인가요?'
                QUERY: MATCH (g:Grade {grade:'4'})<-[:belongs_to]-(p:Person)-[s:SOLVED]->(q:Question)
                RETURN q.code, q.question, AVG(s.time_taken) AS avgTime
                ORDER BY avgTime DESC LIMIT 1""",

                """USER INPUT: '4학년 학생들이 푼 질문 중 정답률이 가장 높은 문제는 무엇인가요?'
                QUERY: MATCH (g:Grade {grade:'4'})<-[:belongs_to]-(p:Person)-[r:SOLVED]->(q:Question)
                RETURN q.code, q.question, AVG(r.is_correct) AS correctRate
                ORDER BY correctRate DESC LIMIT 1""",

                """USER INPUT: '대주제 분수의 덧셈과 뺄셈에 해당하는 문제의 질문 5개를 알고 싶어요.'
                QUERY: MATCH (m:MainTopic {name:'분수의 덧셈과 뺄셈'})-[r:has_question]->(q:Question)
                RETURN q.code, q.question LIMIT 5""",

                """USER INPUT: '배수지가 푼 문제 중 피드백이 포함된 문제의 질문을 알려주세요.'
                QUERY: MATCH (p:Person {name: '배수지'})-[r:SOLVED]->(q:Question)
                WHERE r.feedback IS NOT NULL
                RETURN p, r, q""",

                """USER INPUT: '4학년 학생들이 대주제 약수와 배수의 문제를 얼마나 풀었는지 확인할 수 있나요?'
                QUERY: MATCH (g:Grade {grade:'4'})<-[:belongs_to]-(p:Person)-[s:SOLVED]->(q:Question)<-[:has_question]-(m:MainTopic {name:'큰수'})
                RETURN COUNT(s) AS solveCount"""

                """USER INPUT: '소수의 나눗셈 문제를 잘 못푸는 학생은 어느 대주제를 다시 공부해야 해?'
                QUERY: MATCH (relatedTopic:MainTopic)-[:precedes*]->(t:MainTopic {name: '소수의 나눗셈'})
                RETURN relatedTopic.name;
                """

                """USER INPUT: '변우석 학생 취약 개념 문제 추천해줘'
                QUERY: MATCH (p:Person {name: '변우석'})-[:SOLVED]->(q:Question)<-[:has_question]-(mt:MainTopic)
                MATCH (p)-[s:SOLVED]->(q)
                WITH mt, AVG(s.score) AS avg_score
                ORDER BY avg_score ASC
                LIMIT 1
                WITH mt AS LowestAvgMainTopic, avg_score
                MATCH (p:Person {name: '변우석'})-[:UNSOLVED]->(q:Question)<-[:has_question]-(LowestAvgMainTopic)
                RETURN LowestAvgMainTopic.name AS LowestAvgMainTopic, avg_score, q.question AS UnsolvedQuestions
                """
            ]

            # Text2CypherRetriever 초기화
            retriever = Text2CypherRetriever(
                driver=driver,
                llm=llm,
                neo4j_schema=neo4j_schema,
                examples=examples,
            )

            # GraphRAG 초기화
            rag = GraphRAG(retriever=retriever, llm=llm)

            return {"llm": llm, "retriever": retriever, "rag": rag}, "성공적으로 연결되었습니다!"
        else:
            raise Exception("LLM 연결 실패")
    except Exception as e:
        print(f"오류 발생: {e}")
        return {"llm": None, "retriever": None, "rag": None}, "API Key를 확인해 주세요!"

def generate_query(browser_state, text_input):
    retriever = browser_state["retriever"]

    search_result = retriever.search(query_text=text_input)
    return search_result.metadata['cypher']

def default_llm(browser_state, message):
    llm = browser_state["llm"]

    prompt_text = f"""
    당신은 초등학교 보조 교사 챗봇입니다. user_input에 대답하되 만약 GraphDB 속 정보에 대한 질문이라면 그 질문에 대해 자세한 정보를 답 해주세요.
    그리고 학년, 학생 이름, 대주제 이름, 필터링 기준을 정확히 말하라고 권고해 보세요.
    user_input : {message}
    """
    return llm.invoke(prompt_text).content

def intent_detection(browser_state, message):
    llm = browser_state["llm"]

    prompt_text = f"""
    주어진 query_text 가 학년, 학생, 대주제, 문제에 대한 답변을 받기 위한 본격적인 질문으로 보이면 True를 반환하고, 그렇지 않으면 False를 반환해주세요.
    query_text : {message}
    """
    return llm.invoke(prompt_text).content == 'True'

def response(browser_state, message, chat_history):
    llm = browser_state["llm"]

    if(intent_detection(browser_state, message)):
        rag = browser_state["rag"]
        
        rag_result = rag.search(query_text=message
                                + "(Please also provide evidence for how you used context in your answer. YOU MUST ANSWER in KOREAN PLEASE.)"
                                , return_context = True)
        chat_history.append((message, rag_result.answer))
        return chat_history, rag_result.retriever_result.metadata['cypher'], rag_result.retriever_result.items
    else:
        llm_result = default_llm(browser_state, message)
        chat_history.append((message, llm_result))
        return chat_history, "학년, 학생, 대주제, 문제 관련 질문이었어요.", llm_result

with gr.Blocks(theme=gr.themes.Soft(font=[gr.themes.GoogleFont("Noto Sans Korean")], text_size=gr.themes.sizes.text_lg)) as demo:
    gr.HTML("""
        <div style="text-align: center; max-width: 1000px; margin: 20px auto;">
            <h1>🔗 GraphRAG 실습 워크숍</h1>
        </div>
        """)
    browser_state = gr.State({"llm": None, "retriever": None, "rag": None})

    with gr.Tabs():
        with gr.Tab("API Key 등록"):
            with gr.Row():
                user_api_key = gr.Textbox(label="API Key", placeholder="API Key를 입력해 주세요.", lines=1)
                api_btn = gr.Button("Upload", variant="primary")
            output_text = gr.Textbox(label="API Key 등록 결과", interactive=False)
            api_btn.click(ready_gpt, inputs=user_api_key, outputs = [browser_state, output_text])

        with gr.Tab("강의안"):
            gr.HTML(
                lecture
            )

        with gr.Tab("DB 구조도"):
            gr.HTML(
                structure
            )
        
            gr.Markdown(
                cypher
            )
            
            gr.Button(value='GraphDB 바로가기', link='http://184.72.178.158:7474', variant='primary')
        
        with gr.Tab("예제 생성기"):
            with gr.Row():
                text_input = gr.Textbox(label="질문", placeholder="질문을 입력해 주세요.", lines=2)

                with gr.Column(scale=0):
                  btn = gr.Button("쿼리 생성", variant="primary")
                  clear = gr.Button("Clear")

            output = gr.Textbox(label="생성된 Cypher 쿼리", placeholder="여기에 쿼리가 표시됩니다.", lines=6)
      
            btn.click(generate_query, inputs=[browser_state,text_input], outputs=output)
            clear.click(lambda: None, None, queue=False)

            with gr.Row():
                gr.Button(value='패들릿 바로가기', link='https://padlet.com/02shin00/snu_workshop', variant='primary')

        with gr.Tab("챗봇"):
            with gr.Row():
                with gr.Column(scale=0):
                    generated_query = gr.Textbox(label="생성된 Cypher 쿼리")
                    query_result = gr.Textbox(label="쿼리 조회 결과")

                chatbot = gr.Chatbot()

            with gr.Row():
                with gr.Column():
                    msg = gr.Textbox(
                        placeholder="질문을 입력하세요.",
                        label="입력",
                    )
                with gr.Column(scale=0):
                    btn = gr.Button("Submit", variant="primary")
                    clear = gr.Button("Clear")

            with gr.Row():
                examples = gr.Examples(
                    examples=[
                        "3학년 학생들이 가장 많이 푼 문제의 대주제를 알려줘.",
                        "배수지 학생이 풀지 않은 문제 중 학생들이 많이 푼 문제 3개는 뭐야?",
                    ],
                    inputs=[msg]
                )

            btn.click(fn=response, inputs=[browser_state, msg, chatbot], outputs=[chatbot, generated_query, query_result])
            msg.submit(response, [browser_state, msg, chatbot], [chatbot, generated_query, query_result])
            clear.click(lambda: None, None, msg, queue=False)

demo.launch(debug=True, share=True)
