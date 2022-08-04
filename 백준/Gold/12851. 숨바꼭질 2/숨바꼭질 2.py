import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

graph = [[0,0] for _ in range(100001)]    # [가장 빠른 시간, 방법의 수]


def bfs(graph, start):
    queue = deque()
    queue.append(start)
    graph[start][0] = 0     # 시작점이기 때문에 걸리는 시간 0
    graph[start][1] = 1
    while queue:
        x = queue.popleft() # x는 현재 노드
        if x == K:
            break
        for nx in [x+1, x-1, 2*x]:
            if nx < 0 or nx > 100000:
                continue
            if graph[nx][0] == 0:   # 처음 들르는 경우
                graph[nx][0] = graph[x][0] + 1   # 가는데 1초 걸리기 떄문에
                graph[nx][1] = graph[x][1]       # 가는 방법의 수는 그대로
                queue.append(nx)

            elif graph[nx][0] == graph[x][0] + 1:  # 한 번 이상 들른 경우
                graph[nx][1] += graph[x][1]     # 방법의 수를 더해준다



bfs(graph, N)   # 수빈이의 지점에서 찾기 시작
print(graph[K][0])  # 가장 빠른 시간
print(graph[K][1])  # 가장 빠른 시간으로 찾는 방법의 수
