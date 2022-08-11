# 트리의 개수

"""
트리의 정의 : 1개 이상의 노드로 구성된 사이클이 없는 그래프로 임이의 두 노드 간 하나의 경로만 존재한다
연결 요소는 모든 정점이 서로 연결되어 있는 정점의 부분집합이다.
그래프는 하나 또는 그 이상의 연결 요소로 이루어져 있다.
트리는 사이클이 없는 연결 요소이다.
"""

# 이 문제는 사이클이 아닌 연결요소의 개수를 찾는 것!
# 다른 정점에 연결되어 있지 않은 외딴 정점 또한 트리의 조건에 부합!!!

import sys
from collections import deque


def bfs(start):         # 기존의 bfs와 방문처리를 다르게 해주어야 함
    isTree = True
    queue = deque()
    queue.append(start)
    while queue:
        x = queue.popleft()
        if visited[x]:      # 이미 방문처리가 되어 있다면 (값이 중복되어 큐에 올라가는 경우)
            isTree = False
        visited[x] = True   # 큐에서 값을 꺼내면서 방문처리
        for j in graph[x]:
            if not visited[j]:
                queue.append(j) # 일반적인 경우와 달리 큐에 값을 집어넣자마자 방문처리 해주지 않음
    return isTree



# [[], [2], [1, 3], [2, 4] ,[3], [] , []] -> 3 (노드 1,2,3,4가 연결된 경우)

# [[], [2, 3], [1, 3], [1, 2], [], [], []] -> 3 (노드 1,2,3이 사이클로 연결된 경우)

cases = []  # 각 케이스 마다 트리의 개수가 저장됨

while True:
    n, m = map(int, sys.stdin.readline().split())

    if n == 0 and m ==0:
        break

    count = 0 # 각 테스트 케이스 별 트리의 개수

    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)

    for _ in range(m):  # 각 테스트 케이스의 m개의 간선에 대한 정보
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, n+1): # 1부터 n까지의 노드를 bfs처리를 통해 트리의 개수를 구함
        if visited[i]:      # 예를 들어 노드 1,2,3,4가 연결되어 있다면 1확인하고 바로 5,6확인하면 됨
            continue        # 1,2,3,4 는 이미 방문처리 되어있음
        if bfs(i):
            count += 1

    cases.append(count)



for j in range(len(cases)):
    if cases[j] == 0:
        print("Case {}: No trees.".format(j+1))
    elif cases[j] == 1:
        print("Case {}: There is one tree.".format(j+1))
    elif cases[j] > 1:
        print("Case {}: A forest of {} trees.".format(j+1, cases[j]))
