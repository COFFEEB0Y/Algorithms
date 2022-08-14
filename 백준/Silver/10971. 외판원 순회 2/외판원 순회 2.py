import sys


def tsp(visited, pos):      # 방문기록과 현재 노드의 위치가 인수
    if visited == (1<<n) - 1:       # 모든 도시를 방문한 경우
        return path[pos][0] if path[pos][0] > 0 else sys.maxsize       # 현재 위치에서 처음으로 되돌아가는 비용을 반환
                                                                       # 되돌아갈 수 있는 길인지 또한 확인
    if dp[visited][pos]:    # Memoization
        return dp[visited][pos]

    cost = sys.maxsize

    for city in range(n):
        if visited & (1<<city) == 0 and path[pos][city]: # 방문하지 않았던 도시이고 갈 수 없는 경우가 아니라면 
            new_Ans = path[pos][city] + tsp(visited|(1 << city), city)
            cost = min(cost, new_Ans)

    dp[visited][pos] = cost
    return cost

n = int(sys.stdin.readline())
path = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * n for _ in range((1 << n))]     # Memoization

print(tsp(1, 0))


