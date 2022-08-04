import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

graph = [0 for _ in range(100001)]    # 점의 x좌표만 그래프에 나타내면 된다


def bfs(graph, x):
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        dx = [x, -1, 1]  # 노드가 방문하지 않은 인접한 노드들로 갈 수 있는 경우들 : X-1, X+1, 2*X
        # 큐에서 꺼내는 x좌표의 두 배를 해주어야 한다
        for i in range(3):
            nx = x + dx[i]

            if nx < 0 or nx > 100000:
                continue
            if nx == N:
                continue
            if graph[nx] == 0:  # 방문하지 않은 인접 노드를 만나다면
                graph[nx] = graph[x] + 1   # 시작지점으로부터의 거리를 표시
                queue.append(nx)


bfs(graph, N)   # 수빈이의 지점에서 찾기 시작
print(graph[K]) # 동생이 있는 위치에 표시된 시간을 출력
