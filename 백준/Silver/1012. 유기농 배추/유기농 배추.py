# 유기농 배추

# 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이의 개수 출력 < 단지 문제와 동일 >

import sys
sys.setrecursionlimit(10**7)

T = int(sys.stdin.readline()) # 테스트의 개수

# 상하죄우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(graph, x, y):
    global cnt
    graph[x][y] = 0 # 방문처리
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue

        if graph[nx][ny] == 1:
            dfs(graph, nx, ny)

    return cnt

for _ in range(T):

    M, N, K = map(int, sys.stdin.readline().split())    # 새로운 그래프에 대한 정보를 받음

    cnt = 0 # cnt변수 초기화
    count = [] # 구역 당 1개의 배추흰지렁이 (총 배추읜지렁이의 개수) 다시 빈 리스트로 초기화

    graph = [[0 for _ in range(M)] for _ in range(N)]   # 테스트 케이스마다 새로운 그래프를 그려주어야 함

    for _ in range(K):  # 배추가 심어져 있는 위치를 그래프에 표현
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    for i in range(N):      # 방문했던 0을 1로 바꾸기 때문에 모든 점을 방문해도 중복이 없음
        for j in range(M):
            if graph[i][j] == 1:        # 방문하지 않은 인접한 노드라면
                count.append(dfs(graph, i, j))

    print(len(count))





















