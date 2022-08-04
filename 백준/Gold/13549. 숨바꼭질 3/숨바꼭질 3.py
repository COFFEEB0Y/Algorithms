import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

graph = [0 for _ in range(100001)]    # 점의 x좌표만 그래프에 나타내면 된다

def bfs(graph, start):
    queue = deque()
    queue.append(start)
    while queue:
        x = queue.popleft() # x는 현재 노드
        # 큐에서 꺼내는 x좌표의 두 배를 해주어야 한다
        if x == K:  # 수빈이가 동생을 만난다면
            print(graph[K])
            break   # 또 동생의 좌표롤 움직이는 것을 방지하기 위해
        for nx in [2*x, x-1, x+1]:  # 이동경로마다 걸리는 시간이 다름 (가중치가 다름)
            if nx == 2*x:
                if (0 <= nx <= 100000) and (graph[nx] == 0):  # 방문하지 않은 인접 노드를 만나다면
                    graph[nx] = graph[x]   # 순간이동을 할 때는 시간이 0초이므로 전의 시간 그대로
                    queue.append(nx)
                    # 수빈이가 지나온 위치를 알기 위해 다음 이동 위치에 현재 위치를 기록


            else:
                if (0 <= nx <= 100000) and (graph[nx] == 0):  # 방문하지 않은 인접 노드를 만나다면
                    graph[nx] = graph[x] + 1   # 수빈이가 이동하는데 1초 걸리는 이동방법
                    queue.append(nx)
                    # 수빈이가 지나온 위치를 알기 위해 다음 이동 위치에 현재 위치를 기록



bfs(graph, N)   # 수빈이의 지점에서 찾기 시작


