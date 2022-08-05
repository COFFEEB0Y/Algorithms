# 백트래킹으로 풀기

import sys

N, M = map(int, sys.stdin.readline().split())

s = []

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(1, N+1): # for문 안에 dfs함수가 있다는 점!!
        s.append(i)
        dfs()
        s.pop()


dfs()