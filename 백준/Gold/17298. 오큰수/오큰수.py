# 오큰수 문제
import sys
from collections import deque
N = int(sys.stdin.readline())

while True:
    A = list(map(int, sys.stdin.readline().split()))
    if len(A) == N:
        break

stack = []
result = [-1 for _ in range(N)]  # 오큰수가 존재하지 않으면 -1이기 떄문에 -1로 초기화

for i in range(N):
    try:
        while A[stack[-1]] < A[i]:
            result[stack.pop()] = A[i]
    except:
        pass

    stack.append(i)

print(*result)