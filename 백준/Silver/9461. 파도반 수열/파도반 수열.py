# 파도반 수열

"""
P(1)부터 P(10)까지 첫 10개 숫자는 1, 1, 1, 2, 2, 3, 4, 5, 7, 9이다.

N이 주어졌을 때, P(N)을 구하는 프로그램을 작성하시오.
"""

# 점화식 dp[n] = dp[n-2] + dp[n-3]

import sys

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1

N = int(sys.stdin.readline())
for _ in range(N):
    n = int(sys.stdin.readline())
    if n <= 3:
        print(1)
    else:       # 재귀함수 사용하지 않고 반복문으로 풀기 
        for i in range(4, n+1):
            dp[i] = dp[i-2] + dp[i-3]
        print(dp[n])
