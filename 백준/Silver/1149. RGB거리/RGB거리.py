# RGB 거리

"""
아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값
    1. N번 집의 색은 N-1번 집의 색과 달라야 한다
    2. i번 집의 색은 i-1번, i+1번 집의 색과 달라야 한다
    -> 연속되 번호의 집의 색은 달라야 한다
"""


import sys

N = int(sys.stdin.readline())

# 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다.

cost = [[0, 0, 0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


# 0, 1, 2는 R, G, B를 나타낸다

# cost[i][0] : i번 째 집을 빨강으로 칠했을 때의 최솟값
# cost[i][1] : i번 째 집을 초록으로 칠했을 때의 최솟값
# cost[i][2] : i번 째 집을 파랑으로 칠했을 때의 최솟값

for i in range(1, N+1):
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0]
    cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + cost[i][1]
    cost[i][2] = min(cost[i-1][1], cost[i-1][0]) + cost[i][2]

# 빨강, 초록, 파랑 집을 선택한 모든 경우에 대해서 최솟값만이 나오게 된다. 그 중에서 또 최솟값을 구하면 원하는 답이 나옴
print(min(cost[N][0], cost[N][1], cost[N][2]))