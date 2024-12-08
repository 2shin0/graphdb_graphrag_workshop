lecture = """
          <!DOCTYPE html>
          <html lang="ko">
          <head>
              <meta charset="UTF-8">
              <meta name="viewport" content="width=device-width, initial-scale=1.0">
              <style>
                hr {
                    border: 0;
                    border-top: 2px solid #ccc; 
                    width: 70%;
                    margin: 20px 0;
                }
                h1, h2 {
                    color: #2c3e50;
                    margin-top: 40px !important;
                    overflow: hidden;
                }
                table {
                    width: 70%;
                    border-collapse: collapse;
                }
                th, td {
                    border: 1px solid #ddd;
                    padding: 10px;
                    text-align: left;
                }
                
                .table-container {
                    display: flex;
                    justify-content: space-between;
                }
                table2 {
                    border: 1px solid black;
                    border-collapse: collapse;
                    width: 45%;
                }
                
                th {
                    background-color: #e0e7ff;
                }
                img {
                    max-width: 100%;
                    height: auto;
                }
                .flex-container {
                    display: flex;
                    justify-content: space-around;
                    flex-wrap: wrap;
                    gap: 10px;
                }
                .flex-container img {
                    width: 45%;
                }
                .keywords {
                    background-color: #f9f9f9;
                    padding: 10px;
                    border-left: 4px solid #3498db;
                }
              </style>
          </head>
          <body>
              <h1>✅ Timetable</h1>
              <table>
                  <tr>
                      <th>시간</th>
                      <th>내용</th>
                  </tr>
                  <tr>
                      <td><b>13:00 ~ 13:05</b></td>
                      <td>오프닝, 소개</td>
                  </tr>
                  <tr>
                      <td><b>13:05 ~ 13:15</b></td>
                      <td>- GraphDB, GraphRAG, Prompt Engineering 개념 설명<br>- GraphDB 및 GraphRAG의 교육적 활용 방안 소개</td>
                  </tr>
                  <tr>
                      <td><b>13:15 ~ 13:55</b></td>
                      <td>- 실습 소개<br>- <b>“효과적인 개별화 교육을 위한 교사 보조 챗봇 제작”</b> 실습</td>
                  </tr>
                  <tr>
                      <td><b>13:55 ~ 14:00</b></td>
                      <td>실습 결과 공유 및 마무리</td>
                  </tr>
                  <tr>
                      <td><b>14:00 ~</b></td>
                      <td>질의응답</td>
                  </tr>
              </table>
              <hr>
              <h1>✅ Graph DB (Neo4j)</h1>
              <h2>1. Graph DB란?</h2>
              <p>데이터를 그래프 형태로 저장하는 데이터베이스</p>
              <ul>
                  <li>각 데이터는 노드(Node)로 표현되며, 노드 간의 관계는 엣지(Edge)로 나타냅니다.</li>
              </ul>
              <img src="https://velog.velcdn.com/images/sobit/post/83c6cbc6-11b7-4d8c-8bea-62ecba03688c/image.png" alt="Neo4j 설명" width="45%">
              <h2>2. Graph DB의 요소</h2>
              <table>
                  <tr>
                      <th>요소</th>
                      <th>설명</th>
                  </tr>
                  <tr>
                      <td><b>노드 (Node)</b></td>
                      <td>데이터를 나타내는 엔티티</td>
                  </tr>
                  <tr>
                      <td><b>엣지 (Edge)</b></td>
                      <td>노드 간의 관계를 나타내는 연결선</td>
                  </tr>
                  <tr>
                      <td><b>속성 (Property)</b></td>
                      <td>노드와 엣지에 추가 가능<br>예) 사람 노드에는 이름, 나이, 생일 등의 속성이 있을 수 있습니다.</td>
                  </tr>
                  <tr>
                      <td><b>라벨 (Label)</b></td>
                      <td>노드나 엣지에 대한 그룹을 정의하는 태그, 특정 범주</td>
                  </tr>
              </table>
              <div class="flex-container">
                  <img src="https://velog.velcdn.com/images/sobit/post/e97e5298-f1e6-455e-b601-8ccac4ff3ec3/image.png" alt="Graph 요소 1">
                  <img src="https://velog.velcdn.com/images/sobit/post/99384fed-0c6c-4fb9-a36c-b91fff1b72d2/image.png" alt="Graph 요소 2">
              </div>
              <h2>3. Graph DB의 특징</h2>
              <table>
                  <tr>
                      <th>요소</th>
                      <th>설명</th>
                  </tr>
                  <tr>
                      <td><b>관계 중심 탐색의 효율성</b></td>
                      <td>관계를 직접 모델링하여 복잡한 데이터를 빠르게 탐색</td>
                  </tr>
                  <tr>
                      <td><b>유연한 데이터 모델링</b></td>
                      <td>스키마리스 또는 동적 스키마를 지원하여 데이터 구조 변경이 쉬움</td>
                  </tr>
                  <tr>
                      <td><b>확장성</b></td>
                      <td>데이터가 커질수록 더 빠르게 확장 가능하며, 관계를 중심으로 데이터를 처리하므로 성능이 뛰어남</td>
                  </tr>
              </table>
              <h2>4. Graph DB의 교육적 활용</h2>
              <table>
                  <tr>
                      <th>요소</th>
                      <th>설명</th>
                  </tr>
                  <tr>
                      <td><b>학습 경로 추천 시스템</b></td>
                      <td>학생의 학습 이력과 관심 분야를 바탕으로 학습 경로를 추천하는 시스템 구축</td>
                  </tr>
                  <tr>
                      <td><b>지식 맵 구축</b></td>
                      <td>다양한 교과목이나 주제 간의 관계를 시각화하여, 학생들이 효율적으로 지식을 탐색할 수 있게 돕는 시스템</td>
                  </tr>
                  <tr>
                      <td><b>학생 그룹 분석</b></td>
                      <td>학생들의 학습 데이터를 기반으로 그룹을 분석하고, 각 그룹에 맞는 맞춤형 교육 콘텐츠를 제공</td>
                  </tr>
              </table>
              <div class="keywords">
                  ▶️ <b>키워드</b> : Knowledge Graph, Graph Database, Ontology
              </div>
              <hr>
              <h1>✅ Graph RAG</h1>
              <h2>1. Graph RAG(Graph-based Retrieval-Augmented Generation)란?</h2>
              <p>그래프 데이터베이스를 활용한 검색 기반 생성 모델</p>
              <ul>
                  <li>질문에 대한 답변을 생성할 때 관련 데이터를 그래프에서 검색하여 그 정보를 바탕으로 답변을 생성</li>
              </ul>
              <h2>2. Graph RAG의 특징</h2>
              <ul>
                  <li><b>정확성 향상</b>: 도메인 이해도 ↑, 추론 능력 ↑ ▶️ 생성형 모델의 오류를 줄이고 더 정확한 답변을 자연어로 제공</li>
                  <li><b>확장성과 효율성</b>: 대용량 데이터를 효율적으로 검색하고 처리
                      <p>벡터 데이터베이스는 고차원 공간에서 데이터를 벡터로 표현하고, 유사도를 기반으로 검색</p>
                      <p>반면 그래프 구조는 특정 관계를 빠르게 조회하거나 관련 데이터를 탐색할 때 계산 오버헤드가 적음</p>
                      </ul>
                  </li>
              </ul>
              <hr>
              <h1>✅ 실습 소개</h1>
              <h2>1. In-Context Learning이란?</h2>
              <p>대형 언어 모델이 입력된 예시를 기반으로 새로운 작업을 추론할 수 있게 하는 학습 방법</p>
              <div class="flex-container">
                  <img src="https://velog.velcdn.com/images/sobit/post/f27451e8-4ed2-4206-96ac-3befd0241401/image.png" alt="In-Context Learning 1">
                  <img src="https://velog.velcdn.com/images/sobit/post/d3558a0a-7e61-4ad2-b13e-d5906b9f9323/image.png" alt="In-Context Learning 2">
              </div>
              <h2>2. 챗봇 성능 개선을 위한 예제 생성 실습 설명</h2>
              <p><b>목표</b>: 챗봇 성능 향상을 위해 다양한 예제를 생성하여 모델이 다양한 상황에서 적절하게 반응할 수 있도록 할 수 있다.</p>
              <p>1. <b>GraphDB 구조 이해 및 챗봇 테스트</b>: GraphDB 구조를 이해하고 챗봇의 현재 답변을 테스트 합니다.</p>
              <p>2. <b>예제 추가를 통한 프롬프트 최적화</b>: 예제 생성기를 활용하여 모델이 주어진 질문에 대해 더 정확한 답변을 생성할 수 있도록 프롬프트를 최적화 합니다.</p>
              <p>3. <b>모델 테스트</b>: 챗봇이 사용자의 요구에 맞게 답변을 반환하는지 확인합니다.</p>
            <img src = "https://velog.velcdn.com/images/sobit/post/e8bd5576-4868-4fda-939a-ac939756026d/image.png" alt="실습 구조도">
            """

structure = """
            <!DOCTYPE html>
            <html lang="ko">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    hr {
                        border: 0;
                        border-top: 2px solid #ccc;
                        width: 70%;
                        margin: 20px 0;
                    }
                    h1, h2 {
                        color: #2c3e50;
                        margin-top: 40px !important;
                        overflow: hidden;
                    }
                    table {
                        width: 70%;
                        border-collapse: collapse;
                        margin: 20px 0;
                    }
                    th, td {
                        border: 1px solid #ddd;
                        padding: 10px;
                        text-align: left;
                    }
                    th {
                        background-color: #e0e7ff;
                    }
                    img {
                        max-width: 100%;
                        height: auto;
                    }
                    .flex-container {
                        display: flex;
                        justify-content: space-around;
                        flex-wrap: wrap;
                        gap: 10px;
                    }
                    .flex-container img {
                        width: 45%;
                    }
                    .keywords {
                        background-color: #f9f9f9;
                        padding: 10px;
                        border-left: 4px solid #3498db;
                    }
                    .table-container {
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                    }
                </style>
            </head>
            <body>
            <h2>학생 정보</h2>
            <table>
                <thead>
                    <tr>
                        <th>학년</th>
                        <th>이름</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>3</td><td>김지원</td></tr>
                    <tr><td>3</td><td>이도현</td></tr>
                    <tr><td>4</td><td>배수지</td></tr>
                    <tr><td>4</td><td>남주혁</td></tr>
                    <tr><td>4</td><td>정해인</td></tr>
                    <tr><td>5</td><td>박보영</td></tr>
                    <tr><td>5</td><td>고아라</td></tr>
                    <tr><td>5</td><td>변우석</td></tr>
                    <tr><td>6</td><td>신세경</td></tr>
                    <tr><td>6</td><td>박보검</td></tr>
                </tbody>
            </table>
            <h2>학년별 대주제 정보</h2>
            <table>
                <thead>
                    <tr>
                        <th>학년</th>
                        <th>대주제 코드</th>
                        <th>대주제 이름</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>3</td><td>3A01</td><td>덧셈과 뺄셈</td></tr>
                    <tr><td>3</td><td>3A02</td><td>곱셈</td></tr>
                    <tr><td>3</td><td>3A03</td><td>나눗셈</td></tr>
                    <tr><td>3</td><td>3A04</td><td>분수와 소수</td></tr>
                    <tr><td>3</td><td>3A05</td><td>평면도형</td></tr>
                    <tr><td>3</td><td>3A06</td><td>길이와 시간</td></tr>
                    <tr><td>3</td><td>3A07</td><td>들이와 무게</td></tr>
                    <tr><td>3</td><td>3A08</td><td>자료의 정리</td></tr>
                    <tr><td>4</td><td>4A01</td><td>큰수</td></tr>
                    <tr><td>4</td><td>4A02</td><td>곱셈과 나눗셈</td></tr>
                    <tr><td>4</td><td>4A03</td><td>분수의 덧셈과 뺄셈</td></tr>
                    <tr><td>4</td><td>4A04</td><td>소수의 덧셈과 뺄셈</td></tr>
                    <tr><td>4</td><td>4A05</td><td>규칙 찾기</td></tr>
                    <tr><td>4</td><td>4A06</td><td>도형의 이동</td></tr>
                    <tr><td>4</td><td>4A07</td><td>삼각형</td></tr>
                    <tr><td>4</td><td>4A08</td><td>사각형</td></tr>
                    <tr><td>4</td><td>4A09</td><td>다각형</td></tr>
                    <tr><td>4</td><td>4A10</td><td>각도</td></tr>
                    <tr><td>4</td><td>4A11</td><td>막대그래프와 꺾은선그래프</td></tr>
                    <tr><td>5</td><td>5A01</td><td>자연수의 혼합 계산</td></tr>
                    <tr><td>5</td><td>5A02</td><td>수의 범위와 어림</td></tr>
                    <tr><td>5</td><td>5A03</td><td>약수와 배수</td></tr>
                    <tr><td>5</td><td>5A04</td><td>약분과 통분</td></tr>
                    <tr><td>5</td><td>5A05</td><td>분수의 덧셈과 뺄셈</td></tr>
                    <tr><td>5</td><td>5A06</td><td>분수의 곱셈</td></tr>
                    <tr><td>5</td><td>5A07</td><td>소수의 곱셈</td></tr>
                    <tr><td>5</td><td>5A08</td><td>대응 관계</td></tr>
                    <tr><td>5</td><td>5A09</td><td>합동과 대칭</td></tr>
                    <tr><td>5</td><td>5A10</td><td>직육면체와 정육면체</td></tr>
                    <tr><td>5</td><td>5A11</td><td>다각형의 둘레와 넓이</td></tr>
                    <tr><td>5</td><td>5A12</td><td>평균과 가능성</td></tr>
                    <tr><td>6</td><td>6A01</td><td>분수의 나눗셈</td></tr>
                    <tr><td>6</td><td>6A02</td><td>소수의 나눗셈</td></tr>
                    <tr><td>6</td><td>6A03</td><td>비와 비율</td></tr>
                    <tr><td>6</td><td>6A04</td><td>비례식과 비례배분</td></tr>
                    <tr><td>6</td><td>6A05</td><td>각기둥과 각뿔</td></tr>
                    <tr><td>6</td><td>6A06</td><td>원기둥/원뿔/구</td></tr>
                    <tr><td>6</td><td>6A07</td><td>공간과 입체</td></tr>
                    <tr><td>6</td><td>6A08</td><td>원주율과 원의 넓이</td></tr>
                    <tr><td>6</td><td>6A09</td><td>직육면체와 정육면체의 겉넓이와 부피</td></tr>
                    <tr><td>6</td><td>6A10</td><td>띠그래프와 원그래프</td></tr>
                </tbody>
            </table>
            <h2>대주제 선수-후수학습 관계</h2>
            <table>
                <thead>
                    <tr>
                        <th>선수학습 대주제</th>
                        <th>후수학습 대주제</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>3A01</td><td>3A02</td></tr>
                    <tr><td>3A01</td><td>3A03</td></tr>
                    <tr><td>3A01</td><td>3A03</td></tr>
                    <tr><td>3A03</td><td>3A04</td></tr>
                    <tr><td>3A02</td><td>4A02</td></tr>
                    <tr><td>3A03</td><td>4A02</td></tr>
                    <tr><td>3A04</td><td>4A03</td></tr>
                    <tr><td>3A04</td><td>4A04</td></tr>
                    <tr><td>3A05</td><td>4A06</td></tr>
                    <tr><td>3A05</td><td>4A07</td></tr>
                    <tr><td>3A05</td><td>4A08</td></tr>
                    <tr><td>3A05</td><td>4A09</td></tr>
                    <tr><td>4A07</td><td>4A08</td></tr>
                    <tr><td>4A08</td><td>4A09</td></tr>
                    <tr><td>4A09</td><td>4A10</td></tr>
                    <tr><td>3A08</td><td>4A11</td></tr>
                    <tr><td>4A02</td><td>5A01</td></tr>
                    <tr><td>4A02</td><td>5A03</td></tr>
                    <tr><td>4A02</td><td>5A04</td></tr>
                    <tr><td>4A03</td><td>5A05</td></tr>
                    <tr><td>5A05</td><td>5A06</td></tr>
                    <tr><td>4A04</td><td>5A07</td></tr>
                    <tr><td>4A09</td><td>5A08</td></tr>
                    <tr><td>5A08</td><td>5A09</td></tr>
                    <tr><td>4A09</td><td>5A10</td></tr>
                    <tr><td>5A06</td><td>6A01</td></tr>
                    <tr><td>5A07</td><td>6A02</td></tr>
                    <tr><td>6A03</td><td>6A04</td></tr>
                    <tr><td>5A10</td><td>6A05</td></tr>
                    <tr><td>6A05</td><td>6A06</td></tr>
                    <tr><td>6A06</td><td>6A07</td></tr>
                    <tr><td>6A07</td><td>6A08</td></tr>
                    <tr><td>6A07</td><td>6A09</td></tr>
                    <tr><td>4A11</td><td>6A10</td></tr>
                </tbody>
            </table>
        
            <h2>GraphDB 확인 방법</h2>
            <p>1. "GraphDB 바로가기" 버튼을 클릭합니다.</p>
              <ul>
                  <li>Connect URL : 184.72.178.158:7687</li>
                  <li>Username : neo4j</li>
                  <li>Password : formulas-method-blood</li>
              </ul>
            <p>2. 아래 내용을 참고하여 복사 후 입력창에 붙여 넣습니다.</p>
            <p>3. 실행 버튼 ▶️을 클릭하면 전체 GraphDB를 확인할 수 있습니다.</p>
            </body>
            </html>
            """

cypher = """
            ```Cypher
            # 전체 GraphDB 확인
            MATCH (n)
            RETURN n
            # 5학년 대단원 확인
            MATCH (g5:Grade {grade: '5'})-[:includes]->(m:MainTopic)
            RETURN g5, m
            # 평면도형 단원의 후수 학습 단원 확인
            MATCH (m1:MainTopic {name: '평면도형'})-[:precedes]->(m2:MainTopic)
            RETURN m1, m2;
            # 학생과 학년 확인
            MATCH (p:Person)-[:belongs_to]->(g:Grade)
            RETURN p, g
            # 배수지 학생의 문제 풀이 이력 확인
            MATCH (p:Person {name: "배수지"})-[:SOLVED]->(q:Question)
            RETURN p, q
            UNION
            MATCH (p:Person {name: "배수지"})-[:UNSOLVED]->(q:Question)
            RETURN p, q
            ```
        """
