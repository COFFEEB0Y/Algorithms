# 계단수

"""
길이가 N인 게단 수가 총 몇 개 있는지 찾아보자
계단수 : 인접한 모든 자리의 차이가 1인 수
cf. 0으로 시작하는 수는 계단수가 아니다
"""

# 1, 2, 3 ,4, 5, 6, 7, 8, 9
# 10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98,

# 1~8 뒤에 올 수 있는 숫자는 2개
# 0,9 뒤에 올 수 있는 숫자는 1개


import sys

N = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(N+1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2,N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N]) % 1000000000)