# DFS (깊이 우선 탐색) 그래프 탐색 알고리즘

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)  # 최대 재귀 깊이를 바꿈 < N의 입력 최댓값 : 100000, M의 최대 입력값: 200000 >


def dfs(graph, v, visited):
    global order
    visited[v] = True
    search_sequence[v] = order  # 현재 스택으로 들어간 노드의 탐색 순서를 저장
    order += 1      # 순서를 하나씩 올려준다
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


N, M, R = map(int, input().split())  # R은 시작 노드

graph = [[] for _ in range(N + 1)]  # 인덱스를 맞추기 위해 N+1

search_sequence = [0 for _ in range(N+1)]  # 노드들이 탐색되는 순서를 저장하는 리스트 (시작 노드에서 방문할 수 없는 노드는 0)

visited = [False] * (N + 1)  # 각 노드가 방문된 정보를 리스트 자료형으로 표현 (index 0 때문에 1개 더)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:  # 인접한 노드가 여러 개라면 방문순서는 오름차순이다
    g.sort(reverse= True)

order = 1

dfs(graph, R, visited)

for i in range(1, len(search_sequence)):
    print(search_sequence[i])




