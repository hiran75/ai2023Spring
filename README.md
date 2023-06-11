AI 개발 실무 2차 레포트
레벤슈타인 거리를 이용한 챗봇 구하기



14주차 실습 자료를 참고하여,
기존 TF-IDF와 Consine Similarlity를 이용해 챗봇을 구현한 코드를

레벤슈타인 거리를 기반으로 한 챗봇으로 수정하여 구현



학습 데이터 : 14주차 실습 데이터에 포함된 ChatbotData.csv



과제 상세 설명:  

1. 학습데이터의 질문과 chat의 질문의 유사도를 레벤슈타인 거리를 이용해 구하기
#  학습데이터의 질문과 chat의 질문의 유사도를 레벤슈타인 거리를 이용해 구하기
def calc_Levenshtein_distance(a, b):
        if a == b: return 0 # 같으면 0을 반환
        a_len = len(a) # a 길이
        b_len = len(b) # b 길이
        if a == "": return b_len
        if b == "": return a_len
        # 2차원 표 (a_len+1, b_len+1) 준비하기 --- (※1)
        # matrix 초기화의 예 : [[0, 1, 2, 3], [1, 0, 0, 0, 0], [2, 0, 0, 0, 0], [3, 0, 0, 0, 0], [4, 0, 0, 0, 0]]
        # [0, 1, 2, 3]
        # [1, 0, 0, 0]
        # [2, 0, 0, 0]dk
        # [3, 0, 0, 0] 
        matrix = [[] for i in range(a_len+1)] # 리스트 컴프리헨션을 사용하여 1차원 초기화
        for i in range(a_len+1): # 0으로 초기화
            matrix[i] = [0 for j in range(b_len+1)]  # 리스트 컴프리헨션을 사용하여 2차원 초기화
        # 0일 때 초깃값을 설정
        for i in range(a_len+1):
            matrix[i][0] = i
        for j in range(b_len+1):
            matrix[0][j] = j
        # 표 채우기 --- (※2)
        # print(matrix,'----------')
        for i in range(1, a_len+1):
            ac = a[i-1]
            # print(ac,'=============')
            for j in range(1, b_len+1):
                bc = b[j-1] 
                # print(bc)
                cost = 0 if (ac == bc) else 1  #  파이썬 조건 표현식 예:) result = value1 if condition else value2
                matrix[i][j] = min([
                    matrix[i-1][j] + 1,     # 문자 제거: 위쪽에서 +1
                    matrix[i][j-1] + 1,     # 문자 삽입: 왼쪽 수에서 +1   
                    matrix[i-1][j-1] + cost # 문자 변경: 대각선에서 +1, 문자가 동일하면 대각선 숫자 복사
                ])
                # print(matrix)
            # print(matrix,'----------끝')
        return matrix[a_len][b_len]




2. chat의 질문과 레벤슈타인 거리와 가장 유사한 학습데이터의 질문의 인덱스를 구하기
        # Iterate through the questions and calculate distances
        for i, question in enumerate(self.questions): #질문리스트에서 for를 돌면서 입력문장과 학습데이터 질문과의 유사도 거리를 계산함
            distance = calc_Levenshtein_distance(user_input, question.lower())

            if distance < min_distance: #가장 거리가 작은 질문의 인덱스를 저장함
                min_distance = distance
                best_match_index = i
                
                

3. 학습 데이터의 인덱스의 답을 chat의 답변을 채택한 뒤 출력
![image](https://github.com/hiran75/ai2023Spring/assets/29429137/5e7fcde4-a507-4183-966c-1ed504fc4636)





과제 제출방법: 과제를 구현한 코드를 본인의 github에 올린뒤, github의 주소를 과제로 제출하기
