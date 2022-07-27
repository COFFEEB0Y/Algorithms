# DFS (깊이 우선 탐색) 그래프 탐색 알고리즘 활용
# 1번 컴퓨터가 바이러스에 걸렸을 떄, 1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터의 개수를 구하여라

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)  # 최대 재귀 깊이를 바꿈 < N의 입력 최댓값 : 100000, M의 최대 입력값: 200000 >


def dfs(graph, start, visited):
    global order
    visited[start] = True   # 시작 노드를 방문 처리
    order += 1
    # 해당 노드와 연결된, 아직 방문하지 않은 원소를 방문 처리
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


N = int(input())    # 컴퓨터의 개수(노드의 개수)
M = int(input())    # 네트워크에 연결된 컴퓨터들 (간선)


graph = [[] for _ in range(N + 1)]  # 인덱스를 맞추기 위해 N+1

visited = [False] * (N + 1)  # 각 노드가 방문된 정보를 리스트 자료형으로 표현 (index 0 때문에 1개 더)

for _ in range(M):      # 그래프 내의 노드들이 어떤 노드들과 연결되어 있는지
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:  # 인접한 노드가 여러 개라면 방문순서는 내림차순이다
    g.sort()

order = 0   # 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 구하는 것이므로 1번 컴퓨터는 제외

dfs(graph, 1, visited)  # 문제의 조건이 1번 컴퓨터가 바이러스에 걸렸을 때

# search_sequence에서 0인 노드들은 1번 컴퓨터에 연결되어 있지 않은 컴퓨터들이으로 제외

print(order-1)




