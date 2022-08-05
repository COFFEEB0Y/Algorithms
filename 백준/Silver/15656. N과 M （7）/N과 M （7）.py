# 백트래킹으로 풀기

import sys

N, M = map(int, sys.stdin.readline().split())
Ns = list(map(int, sys.stdin.readline().split()))
Ns.sort()

s = []  # stack


def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in Ns: # 수열 Ns안에 있는 수들
            s.append(i)
            dfs()
            s.pop()


dfs()