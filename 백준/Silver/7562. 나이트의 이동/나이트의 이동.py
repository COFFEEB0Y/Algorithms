# 나이트의 이동

"""나이트가 최소 몇 번만에 이동할 수 있는지 출력한다"""
# 최소 횟수를 다루는 문제이므로 bfs 사용!
import sys
from collections import deque

def bfs(s_y, s_x, e_y, e_x):

    dy = [-1, 1, 2, 2, 1, -1, -2, -2]
    dx = [2, 2, 1, -1, -2, -2, -1, 1]

    queue = deque()
    queue.append((s_y, s_x))
    while queue:
        y, x = queue.popleft()
        if y == e_y and x == e_x:
            return graph[y][x] - 1

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < I and 0 <= ny < I and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((ny, nx))


T = int(sys.stdin.readline())

for _ in range(T):
    I = int(sys.stdin.readline())
    start_y, start_x = map(int, sys.stdin.readline().split())
    end_y, end_x = map(int, sys.stdin.readline().split())

    graph = [[0 for _ in range(I)] for _ in range(I)]

    graph[start_y][start_x] = 1     # 시작 부분은 방문처리 (다시 시작점으로 돌아가면 안되기 떄문)

    answer = bfs(start_y, start_x, end_y, end_x)
    print(answer)


