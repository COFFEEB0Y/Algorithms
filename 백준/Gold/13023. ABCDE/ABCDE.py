# ABCDE

"""즉, 정점 V를 골라 DFS를 진행했을 때 깊이가 4인 경우가 있는지 확인하며 출력하면 된다."""

import sys

def dfs(start, depth):
    if depth == 4:          # 깊이가 4이상이라면 1출력하고 종료
        print(1)
        exit()
    for i in relation[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth + 1)
            visited[i] = False


N, M = map(int, sys.stdin.readline().split())

relation = [[] for _ in range(N)]
visited = [False] * N

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    relation[a].append(b)
    relation[b].append(a)

for i in range(N):      # 모든 노드들을 돌아가면서 깊이 측정
    visited[i] = True   # 자기 자신 또한 방문처리를 초기화시켜줌
    dfs(i, 0)
    visited[i] = False  # 방문처리를 다시 초기화

print(0)
