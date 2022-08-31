# 섬의 개수


import sys
sys.setrecursionlimit(10**7)

def dfs(y, x):
    graph[y][x] = 0

    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if ny < 0 or nx < 0 or ny >= h or nx >= w:
            continue

        if graph[ny][nx] == 1:
            dfs(ny, nx)


while True:
    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        break

    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 0:
                continue
            dfs(i, j)
            cnt += 1
    print(cnt)