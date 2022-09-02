# 알고스팟

"""현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동하려면 벽을 최소 몇 개 부수어야 하는지 구하는 프로그램을 작성하시오."""'' \

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(M)]

visited = [[-1] * N for _ in range(M)]  # 방문처리를 하는 그래프


def bfs():
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 0     # 현재 (1,1)에 있는 알고스팟이 있는 곳 방문처리
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if nx < 0 or ny < 0 or ny >= M or nx >= N:
                continue

            if visited[ny][nx] == -1:   # 가중치가 있는 edge 0->0 : 0, 0->1 : 1, 1->1 : 1
                if graph[ny][nx] == 0:      # 주변에 0이 있으면 먼저 가야 됨
                    visited[ny][nx] = visited[y][x]
                    queue.appendleft((ny, nx))      # appendleft로 먼저 처리

                elif graph[ny][nx] == 1:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny, nx))

bfs()
print(visited[M-1][N-1])
