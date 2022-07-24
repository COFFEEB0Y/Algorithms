# DFS (깊이 우선 탐색) 그래프 탐색 알고리즘

import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)  # 최대 재귀 깊이를 바꿈 < N의 입력 최댓값 : 100000, M의 최대 입력값: 200000 >


def bfs(graph, start, visited):
    global order
    queue = deque([start])
    visited[start] = True   # 시작 노드를 삽입 후 방문 처리
    while queue:    # 큐가 빌 떄까지 반복
        # 큐에서 하나의 노드를 뽑아 출력
        v = queue.popleft()
        search_sequence[v] = order  # 노드가 탐색되는 순서를 저장
        order += 1
    # 해당 노드와 연결된, 아직 방문하지 않은 원소들을 큐애 삽입 후 방문 처리
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


N, M, R = map(int, input().split())  # R은 시작 노드

graph = [[] for _ in range(N + 1)]  # 인덱스를 맞추기 위해 N+1

search_sequence = [0 for _ in range(N+1)]  # 노드들이 탐색되는 순서를 저장하는 리스트 (시작 노드에서 방문할 수 없는 노드는 0)

visited = [False] * (N + 1)  # 각 노드가 방문된 정보를 리스트 자료형으로 표현 (index 0 때문에 1개 더)

for _ in range(M):      # 그래프 내의 노드들이 어떤 노드들과 연결되어 있는지
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:  # 인접한 노드가 여러 개라면 방문순서는 내림차순이다
    g.sort(reverse= True)

order = 1

bfs(graph, R, visited)

for i in range(1, len(search_sequence)):
    print(search_sequence[i])




