import pandas as pd

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


class SimpleChatBot:

    def __init__(self, filepath):
        self.questions, self.answers , self.data= self.load_data(filepath)

    #챗봇의 학습데이터를 읽어오기
    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        questions = data['Q'].tolist()  # 질문열만 뽑아 파이썬 리스트로 저장
        answers = data['A'].tolist()   # 답변열만 뽑아 파이썬 리스트로 저장
        return questions, answers, data

    ################chat의 질문과 레벤슈타인 거리와 가장 유사한 학습데이터의 질문의 인덱스를 구하기
    # #######################
    def find_answer(self, input_sentence):
        # Convert user input to lowercase
        user_input = input_sentence.lower()
        best_match_index = None
        min_distance = float('inf')

        # Iterate through the questions and calculate distances
        for i, question in enumerate(self.questions): #질문리스트에서 for를 돌면서 입력문장과 학습데이터 질문과의 유사도 거리를 계산함
            distance = calc_Levenshtein_distance(user_input, question.lower())

            if distance < min_distance: #가장 거리가 작은 질문의 인덱스를 저장함
                min_distance = distance
                best_match_index = i
        
            # 최종 질문인덱스의 best_match_index의 답변 answer text를 돌려줌
        response = self.answers[best_match_index] if best_match_index is not None else "죄송합니다. 정확한 답변을 찾지 못했습니다."
        return response
        
   

# CSV 파일 경로를 지정하세요.
filepath = 'ChatbotData.csv'

# 간단한 챗봇 인스턴스를 생성합니다.
chatbot = SimpleChatBot(filepath)

# '종료'라는 단어가 입력될 때까지 챗봇과의 대화를 반복합니다.
while True:
    input_sentence = input('You: ')
    if input_sentence.lower() == '종료':
        break
    response = chatbot.find_answer(input_sentence)
    print('Chatbot:', response)
    
