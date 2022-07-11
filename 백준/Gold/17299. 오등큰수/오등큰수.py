# 오큰수 문제
import sys
from collections import Counter
from collections import deque

N = int(sys.stdin.readline())

while True:
    A = list(map(int, sys.stdin.readline().split()))
    if len(A) == N:  # 수열 A의 크기는 N과 같다
        break

stack = []
result = [-1 for _ in range(N)]  # 오등큰수가 존재하지 않으면 -1이기 떄문에 -1로 초기화

count = Counter(A)

for i in range(N):
    try:
        while count[A[stack[-1]]] < count[A[i]]:        # 등장한 횟수를 서로 비교 (index 1)
            result[stack.pop()] = A[i]      # 등장한 횟수가 큰 수중에서 가장 왼쪽에 있는 수
    except:
        pass        # 처음에 index로 0 이 들어오면 IndexError가 나는 것을 방지

    stack.append(i)

print(*result)

