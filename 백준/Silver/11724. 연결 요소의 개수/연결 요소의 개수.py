# 연결 요소의 개수

import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

# 그래프의 연결요소 개수를 구하기에 앞서 그래프 그리기

graph = [[] for _ in range(N+1)]
visited = [True] + [False] * N
count = 0   # 연결요소의 개수


def dfs(start):
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            dfs(node)


for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    if visited[i]:
        continue
    dfs(i)
    count += 1

print(count)
