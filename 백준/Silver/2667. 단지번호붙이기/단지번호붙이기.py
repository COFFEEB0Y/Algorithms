# 백준 2267 (단지 번호 붙이기)
"""
DFS로 풀기
그래프가 상하좌우로 연결되어 있다고 가정
전체를 돌면서 1인 부분을 탐색
다시 방문하지 않도록 0으로 방문처리
"""

import sys

N = int(sys.stdin.readline())  # 지도의 크기 N (5<=N<=25)

graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]       # 2차원 리스트로 그래프 작성

cnt = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(graph, x, y):
    global cnt
    graph[x][y] = 0 # 방문처리
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue

        if graph[nx][ny] == 1:
            dfs(graph, nx, ny)

    return cnt

count = [] # 단지 내의 집의 수를 저장하는 리스트
result = [] # 우리가 출력해야 하는 값

for i in range(N):      # 방문했던 0을 1로 바꾸기 때문에 모든 점을 방문해도 중복이 없음
    for j in range(N):
        if graph[i][j] == 1:        # 방문하지 않은 인접한 노드라면
            count.append(dfs(graph, i, j))

for i in range(len(count)):
    if i == 0:
        result.append(count[i])
    else:
        result.append(count[i]-count[i-1])
result.sort()
print(len(result))
for i in result:
    print(i)


