# 구간 합 구하기 5 (누적합 2차원인 경우)
# <참조. https://castlerain.tistory.com/100>
import sys

N, M = map(int, sys.stdin.readline().split())

data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

prefix_sum = [[0 for _ in range(N+1)] for _ in range(N+1)]
# 문제에서 말하는 (2, 2)는 graph[1,1]의 수를 의미함

# 누적합 구하기'
for i in range(1, N+1):
    for j in range(1, N+1):
        prefix_sum[i][j] = prefix_sum[i][j-1] + prefix_sum[i-1][j] - prefix_sum[i-1][j-1] + data[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    interval_sum = prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1]
    print(interval_sum)