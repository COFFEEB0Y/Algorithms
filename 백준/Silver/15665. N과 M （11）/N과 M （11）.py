import sys
from itertools import  combinations
N, M = map(int, sys.stdin.readline().split())
lst = sorted(list(map(int, sys.stdin.readline().split())))

# 백트래킹으로 풀기

s = []
result = set()    # 중복되는 순열은 출력하지 않기 위해

def dfs():
    if len(s) == M:
        result.add(tuple(s))
        return

    for i in range(N):
        s.append(lst[i])
        dfs()
        s.pop()


dfs()
for i in sorted(result):    # 순열은 오름차순으로 출력된다 
    print(*i)
