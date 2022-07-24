# DFS와 BFS 문제
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)  # 최대 재귀 깊이를 바꿈 < N의 입력 최댓값 : 100000, M의 최대 입력값: 200000 >


def dfs(graph, start, visited):
    dfs_visited[start] = True   # 시작 노드를 방문 처리
    dfs_order.append(start)
    # 해당 노드와 연결된, 아직 방문하지 않은 원소를 방문 처리
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True # 현재 노드를 방문 처리
    while queue:
        v = queue.popleft()
        bfs_order.append(v)
        for i in graph[v]:  # 큐에서 뺀 노드와 인접한 노드들 중
            if not visited[i]:
                queue.append(i)     # 방문하지 않은 인접 노드들이 여러개라면 모두 큐에 삽잉
                visited[i] = True   # 삽입한 노드를 방문처리


N, M, V = map(int, input().split())     # V는 시작 노드


graph = [[] for _ in range(N + 1)]  # 인덱스를 맞추기 위해 N+1

dfs_visited = [False] * (N + 1)  # 각 노드가 방문된 정보를 리스트 자료형으로 표현 (index 0 때문에 1개 더)
bfs_visited = [False] * (N + 1)  # 각 노드가 방문된 정보를 리스트 자료형으로 표현 (index 0 때문에 1개 더)

for _ in range(M):      # 그래프 내의 노드들이 어떤 노드들과 연결되어 있는지
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:  # 인접한 노드가 여러 개라면 방문순서는 오름차순이다
    g.sort()


dfs_order = [] # dfs 탐색 순서 저장 변수
bfs_order = [] # bfs 탐색 순서 저장 변수

dfs(graph, V, dfs_visited)
bfs(graph, V, bfs_visited)


print(*dfs_order)
print(*bfs_order)






