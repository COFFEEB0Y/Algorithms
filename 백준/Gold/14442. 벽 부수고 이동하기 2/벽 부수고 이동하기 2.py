# 벽 부수고 이동하기 2

"""
시작하는 칸과 끝나는 칸도 포함해서 센다.
만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 K개 까지 부수고 이동하여도 된다.
맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.
"""

import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())

# 벽을 만났는지 여부는 graph에서 확인 / 방문했던 길인지는 visited에서 확인 / 경로를 기록하는 것도 visited에
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

# 방문처리하고 경로를 모두 visited에 기록
# K개의 층을 모두 0으로 초기화
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1


def bfs(s_y, s_x, crash_wall):
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    queue = deque()
    queue.append((s_y, s_x, crash_wall))

    while queue:
        y, x, crash_wall = queue.popleft()

        if y == N - 1 and x == M - 1:
            return visited[y][x][crash_wall]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if (0 <= ny < N) and (0 <= nx < M):

                # 벽이 아닌 길을 만났다
                if graph[ny][nx] == 0 and visited[ny][nx][crash_wall] == 0:
                    visited[ny][nx][crash_wall] = visited[y][x][crash_wall] + 1  # 방문처리 + 경로 기록 (0층에 기록)
                    queue.append((ny, nx, crash_wall))

                # 벽을 만났는데 벽을 부순 횟수가 K번 이하인 경우
                if graph[ny][nx] == 1 and crash_wall < K and visited[ny][nx][crash_wall +1] == 0:
                    # 만약에 K가 1이면 0층(한번도 안부순 경우) 1층(한 번 벽을 부순 경우) 이렇게 2개의 z좌표가 만들어짐
                    # 1번 벽을 부쉈다면 더 이상 벽을 부술 수 없다 crash_wall이 1이면 벽이 있는 길을 지나갈 수 없음
                    visited[ny][nx][crash_wall + 1] = visited[y][x][crash_wall] + 1  # 방문처리 + 경로 기록 (1층에 기록)
                    queue.append((ny, nx, crash_wall + 1))
    # 목적 지점까지 도달하지 못한다면
    return -1
 # graph[0, 0] 에서 시작하고 벽을 부딫친 횟수가 0이다
print(bfs(0, 0, 0))

