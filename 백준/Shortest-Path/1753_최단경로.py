"""
다익스트라 알고리즘
- 하나의 노드에서 다른 모든 노드까지의 거리를 구할 수 있다
다익스트라 알고리즘의 원리
- 최단거리를 구할 노드에서 시작하여, 거리가 입력된 노드 중 최단거리가 가장 작은 노드를 돌아가며 선택
- 노드를 돌아가면서, 더 거리가 나오면 값을 갱신하여 넣습니다
"""

# n, m = map(int, input().split())
# k = int(input())                 # 시작할 노드
# INF = 1e8

# graph = [[] for _ in range(n+1)] # 1번 노드부터 시작하므로 하나더 추가

# visited = [False] * (n+1)
# distance = [INF] * (n+1)

# for _ in range(m):
#   u, v, w = map(int, input().split()) # u: 출발노드, v: 도착노드, w: 연결된 간선의 가중치 
#   graph[u].append((v, w))             # 거리 정보와 도착노드를 같이 입력합니다.

# def get_smallest_node():
#   min_val = INF
#   index = 0
#   for i in range(1, n+1):
#     if distance[i] < min_val and not visited[i]: 
#       min_val = distance[i]
#       index = i
#   return index

# def dijkstra(start):
#   distance[start] = 0 # 시작 노드는 0으로 초기화
#   visited[start] = True

#   for i in graph[start]:
#     distance[i[0]] = i[1] # 시작 노드와 연결된 노도들의 거리 입력
  
#   for _ in range(n-1): 
#     now = get_smallest_node() # 거리가 구해진 노드 중 가장 짧은 거리인 것을 선택
#     visited[now] = True       # 방문 처리

#     for j in graph[now]:
#       if distance[now] + j[1] < distance[j[0]]: # 기5존에 입력된 값보다 더 작은 거리가 나온다면,
#         distance[j[0]]= distance[now] + j[1]    # 값을 갱신한다.

# dijkstra(k)
# print(distance)

# for i in distance[1:]:
#     if i == INF:
#         print("INF")
#     else:
#         print(i)


# heap 자료구조를 활용하면 시간복잡도를 낮출 수 있다
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
k = int(input())                 # 시작할 노드
INF = 1e8

graph = [[] for _ in range(n+1)] # 1번 노드부터 시작하므로 하나더 추가

distance = [INF] * (n+1)

for _ in range(m):
  u, v, w = map(int, input().split()) # u: 출발노드, v: 도착노드, w: 연결된 간선의 가중치 
  graph[u].append((v, w))             # 거리 정보와 도착노드를 같이 입력합니다.


import heapq

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start)) # 우선순위, 값 형태로 들어간다. (이 문제에서는 우선순위가 간선 간의 가중치)
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q) # 우선순위가 가장 낮은 값(가장 작은 거리)이 나온다.

    if distance[now] < dist: # 이미 입력되어있는 값이 현재노드까지의 거리보다 작다면 이미 방문한 노드이다.
      continue               # 따라서 다음으로 넘어간다.

    for next_node, w in graph[now]:     # 연결된 모든 노드 탐색
      if dist+w < distance[next_node]: # 기존에 입력되어있는 값보다 크다면
        distance[next_node] = dist+w   
        heapq.heappush(q, (dist+w, next_node))

dijkstra(k)

for i in distance[1:]:
    print("INF" if i == INF else i) 