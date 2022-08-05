# 백트래킹으로 풀기

import sys

N, M = map(int, sys.stdin.readline().split())

s = []

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    if len(s) == 0:
        z = 0
    else:
        z = max(s)

    for i in range(1, N+1): # for문 안에 dfs함수가 있다는 점!!
        if i >= z:  # 수열이 비내림차순이다
            s.append(i)
            dfs()
            s.pop()


dfs()