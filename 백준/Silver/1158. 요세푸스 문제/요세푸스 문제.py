import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
deque = deque(i for i in range(1, N+1))
answer = []

while len(deque) > 0:
    for _ in range(K-1):     # K 번째 사람을 덱의 맨 왼쪽에 놓는게 핵심
        deque.append(deque.popleft())
    answer.append(str(deque.popleft()))  # K 번째 사람을 완전 소거
result = ', '.join(answer)
print('<' + result + '>')
