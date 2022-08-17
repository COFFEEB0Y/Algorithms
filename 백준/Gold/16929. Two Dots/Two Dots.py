# Two Dots - 그래프 문제

import sys

"""
이 함수의 목적:
cycle을 이룬다면 True를 반환
cycle을 이루지 못한다면 False를 반환
"""
def dfs(x, y, px, py, dot_color):
    # 이미 방문했던 점이라면 cycle을 이룸 but 바로 이전의 점인 경우는 제외
    if visited[x][y] == 1:  # 방문 여부를 여기서 물어봄 -> #A에서 물어봤다면 이미 방문했던 노드를 다시 들어가지 못함
        return True
    visited[x][y] = 1

    for i in range(4):  # 상하좌우로 이동할 수 있음

        nx = x + dx[i]  # x좌표가 y축 이동을 담당
        ny = y + dy[i]  # y좌표가 x축 이동을 담당

        if nx != px or ny != py:  # 바로 이전의 점이 아니라면

            if nx < 0 or ny < 0 or nx >= N or ny >= M: # 노드가 그래프의 범위를 벗어나는 경우
                continue

            if graph[nx][ny] == dot_color:    #A 인접한 점이 같은 색깔의 점이라면 (방문했는지를 여기서 물어보지 않음)
                if dfs(nx, ny, x, y, dot_color):
                    return True
    return False


N, M = map(int, sys.stdin.readline().split())
graph = [list(map(str, input())) for _ in range(N)]    # 그래프 그리기
visited = [[0] * M for _ in range(N)]


dx = [1, 0, -1, 0]      # vertax가 이동할 수 있는 방향
dy = [0, 1, 0, -1]

flag = False
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        if dfs(i, j, 0, 0, graph[i][j]):
            flag = True
            break
print('Yes') if flag else print('No')


