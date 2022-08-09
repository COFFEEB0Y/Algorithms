# 트리의 부모 찾기


import sys
sys.setrecursionlimit(10**9)
N = int(sys.stdin.readline())   # 총 노드의 개수

# dfs를 사용하여 노드들간의 서열 파악 (누가 자식이고 누가 부모인지)

Parent = [0 for _ in range(N+1)]    # 부모 노드를 기록함과 동시에 방문처리

graph = [[] for _ in range(N+1)]    # 그래프 그리기

# 서로 연결된 노드를 알려주는 graph
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    for i in graph[start]:
        if Parent[i] == 0:
            Parent[i] = start # 부모노드를 기록
            dfs(i)
dfs(1)

print(*Parent[2:], sep='\n')





