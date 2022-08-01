# 미로 탐색
# BFS -> 지나야 하는 최소의 칸 수를 출력

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# (N, M)의 위치로 이동하는 경로

def bfs(graph, x, y):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1        # 지나간 길에 1씩 더하면서 지나감 < 최단거리를 기록하면서 이동 >
                queue.append((nx, ny))                 # 그래프의 지나갈 수 있는 모든 점에 시작점으로부터의 거리를 기록

    return graph[N-1][M-1]  # 끝점의 최단거리값을 출력

print(bfs(graph, 0, 0))  # 최적경로가 아닌 길들을 제거해주어야 함





