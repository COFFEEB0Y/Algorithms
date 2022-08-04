import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

graph = [0 for _ in range(100001)]    # 점의 x좌표만 그래프에 나타내면 된다

path = [0 for _ in range(100001)]     # 수빈이가 다음으로 이동할 위치 인덱스에 현재 위치를 표시해주는 역할

def sequence(K): # 동생이 있는 위치를 인자로 받음
    """
    동생이 있는 위치까지 수빈이가 어떻게 이동했는지 알려주는 함수
    역추적 방식 : 전의 위치가 현재 위치에 기록되어 있다는 점을 이용
    """
    data = [K]
    for _ in range(graph[K]):
        data.append(path[K])
        K = path[K]
    data = list(reversed(data))
    return data







def bfs(graph, start):
    queue = deque()
    queue.append(start)
    while queue:
        x = queue.popleft() # x는 현재 노드
        dx = [x, -1, 1]  # 노드가 방문하지 않은 인접한 노드들로 갈 수 있는 경우들 : X-1, X+1, 2*X
        # 큐에서 꺼내는 x좌표의 두 배를 해주어야 한다
        if x == K:  # 수빈이가 동생을 만난다면
            print(graph[K])
            print(*sequence(K))
        for i in range(3):
            nx = x + dx[i]  # nx가 수빈이가 이동한 좌표

            if nx < 0 or nx > 100000:
                continue
            if nx == N:
                continue
            if graph[nx] == 0:  # 방문하지 않은 인접 노드를 만나다면
                graph[nx] = graph[x] + 1   # 전의 노드 + 1 : 시작지점으로부터 이동한 시간을 표시
                queue.append(nx)
                # 수빈이가 지나온 위치를 알기 위해 다음 이동 위치에 현재 위치를 기록
                path[nx] = x



bfs(graph, N)   # 수빈이의 지점에서 찾기 시작


