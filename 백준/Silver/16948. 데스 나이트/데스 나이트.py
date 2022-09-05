# 데스 나이트

"""
데스 나이트가 있는 곳이 (r, c)라면, (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)로 이동할 수 있다.
데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 구해보자
최소횟수 -> BFS
"""

import sys
from collections import deque
N = int(sys.stdin.readline())

graph = [[0] * N for _ in range(N)]

r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
# 시작점을 1로 초기화 (방문처리 편하게 하기 위해 = 0과 충돌하지 않기 위해)
graph[r1][c1] = 1

def bfs(start_y, start_x):
    queue = deque()
    queue.append((start_y, start_x))
    # 나이드가 움직일 수 있는 이동경로
    dy = [-2, -2, 0, 0, 2, 2]
    dx = [-1, 1, -2, 2, -1, 1]

    while queue:
        y, x = queue.popleft()

        for i in range(6):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < N and graph[ny][nx] == 0:
                queue.append((ny, nx))
                graph[ny][nx] = graph[y][x] + 1

bfs(r1, c1)
# 시작점을 1로 방문처리했기 때문에 나중에 -1해주기
print(graph[r2][c2]-1)
# 이동할 수 없는 경우에는 -1이 출력됨 -> graph[r2][c2]가 0일 것이기 때문에