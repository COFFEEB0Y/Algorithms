# 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라
# 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다.

# 1 : 익은 토마토
# 0 : 익지 않은 토마토
# -1 : 토마토가 들어있지 않은 칸

import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

# 큐 생성
queue = deque([])

# 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미 cf.대각선이 있다면 추가
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
# 먼저 익은 토마토들을 큐에 집어넣기 (처음의 그래프에서 1인 노드들)
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i,j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            # 상하좌우 이동하면서 방문기록이 없고(이 문제에서는 0) 그래프의 범위를 벗어나지 않는 노드들을 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            # nx가 행을 담당, ny가 열을 담당 -> 항상 주의!
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                # 조건을 만족하는 경우 방문처리 후 큐에 추가
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])


# 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
# bfs를 수행한 후 그래프 내에 0이 남아있는 경우
bfs()
res = 0 # 결과값을 저장하는 변수
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
# 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력
print(res-1)




