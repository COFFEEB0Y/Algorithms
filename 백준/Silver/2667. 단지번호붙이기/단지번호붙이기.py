# 백준 2267 (단지 번호 붙이기)
"""
BFS로 풀기
그래프가 상하좌우로 연결되어 있다고 가정
전체를 돌면서 1인 부분을 탐색
다시 방문하지 않도록 0으로 방문처리
"""

import sys
from collections import deque

N = int(sys.stdin.readline())  # 지도의 크기 N (5<=N<=25)

graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]       # 2차원 리스트로 그래프 작성

def bfs(graph, x, y):
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    return cnt

count = [] # 단지 내의 집의 수를 저장하는 리스트

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count.append(bfs(graph, i, j))

count.sort() # 각 단지에 속하는 집의 수를 오름차순으로 정렬
print(len(count))
for i in count:
    print(i)


