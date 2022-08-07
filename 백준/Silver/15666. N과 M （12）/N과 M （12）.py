import sys
from itertools import  combinations
N, M = map(int, sys.stdin.readline().split())
lst = sorted(list(map(int, sys.stdin.readline().split())))

# 백트래킹으로 풀기

s = []
result = set()

def dfs():
    if len(s) == M:
        result.add(tuple(s))
        return

    if len(s) == 0:
        z = 0
    else:
        z = max(s)

    for i in range(N):
        if lst[i] >= z:
            s.append(lst[i])
            dfs()
            s.pop()


dfs()
for i in sorted(result):
    print(*i)
