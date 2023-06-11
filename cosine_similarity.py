from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# TfidfVectorizer 객체 생성
vectorizer = TfidfVectorizer()

# 레벤슈타인 거리 구하기
def calc_distance(a, b):
    ''' 레벤슈타인 거리 계산하기 '''
    if a == b: return 0 # 같으면 0을 반환
    a_len = len(a) # a 길이
    b_len = len(b) # b 길이
    if a == "": return b_len
    if b == "": return a_len
    # 2차원 표 (a_len+1, b_len+1) 준비하기 --- (※1)
    # matrix 초기화의 예 : [[0, 1, 2, 3], [1, 0, 0, 0, 0], [2, 0, 0, 0, 0], [3, 0, 0, 0, 0], [4, 0, 0, 0, 0]]
    # [0, 1, 2, 3]
    # [1, 0, 0, 0]
    # [2, 0, 0, 0]
    # [3, 0, 0, 0] 
    matrix = [[] for i in range(a_len+1)] # 리스트 컴프리헨션을 사용하여 1차원 초기화
    for i in range(a_len+1): # 0으로 초기화
        matrix[i] = [0 for j in range(b_len+1)]  # 리스트 컴프리헨션을 사용하여 2차원 초기화
    # 0일 때 초깃값을 설정
    for i in range(a_len+1):
        matrix[i][0] = i
    for j in range(b_len+1):
        matrix[0][j] = j
     #표 채우기 --- (※2)
    print(matrix,'----------')


    for i in range(1, a_len+1):
        ac = a[i-1]
        print(ac,'=============')
        for j in range(1, b_len+1):
            bc = b[j-1] 
            print(bc)
            cost = 0 if (ac == bc) else 1  #  파이썬 조건 표현식 예:) result = value1 if condition else value2
            matrix[i][j] = min([
                matrix[i-1][j] + 1,     # 문자 제거: 위쪽에서 +1
                matrix[i][j-1] + 1,     # 문자 삽입: 왼쪽 수에서 +1   
                matrix[i-1][j-1] + cost # 문자 변경: 대각선에서 +1, 문자가 동일하면 대각선 숫자 복사
            ])
            # print(matrix)
        # print(matrix,'----------끝')
    return matrix[a_len][b_len]


# 한국어 문장들
doc1 = "나는 학교에 갔다"
doc2 = "나는 영화관에 갔다"
# sentence2 = "너는 그제 밥을 지었습니다."

# 문장들을 벡터화
tfidf_matrix = vectorizer.fit_transform([doc1, doc2]) # Scipy의 CSR(Compressed Sparse Row) 형식의 희소 행렬(sparse matrix), 이 형식은 2차원 배열의 데이터를 메모리 효율적으로 저장하기 위해 0이 아닌 값들만을 저장  

# print( tfidf_matrix.toarray())

# 문장1과 문장2의 코사인 유사도 계산
cosine_sim = calc_distance(tfidf_matrix[0:1], tfidf_matrix[1:2]) # tfidf_matrix[0:1]는 첫 번째 행을 선택하는 슬라이싱
print(cosine_sim, type(cosine_sim))

print(f"문장 1: {doc1}")
print(f"문장 2: {doc2}")
print(f"두 문장의 코사인 유사도: {cosine_sim[0][0]}")