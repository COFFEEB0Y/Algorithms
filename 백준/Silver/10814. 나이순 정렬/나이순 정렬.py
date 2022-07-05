import sys

N = int(sys.stdin.readline())
age_list = [0] * N

for i in range(N):
    age, name = sys.stdin.readline().split() # 나이, 이름, 가입한 순서를 각 사람마다 지정
    age_list[i] = int(age), name, i+1        # 여러 개의 요소를 하나의 인덱스 공간에 집어넣기

age_list.sort(key= lambda x: (x[0], x[2]))  # 나이 순으로, 나이가 같다면 가입 순서로 정렬

for i in range(len(age_list)):
    print(age_list[i][0], age_list[i][1]) # 이름과 나이를 출력

