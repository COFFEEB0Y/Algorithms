# 01타일

""" N이 주어졌을 때 지원이가 만들 수 있는 모든 가짓수를 세는 것이다"""

import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

if N <= 2:
    print(dp[N])
else:
    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746 # 점화식 dp[n] = dp[n-1] + dp[n-2]
    print(dp[N])

# 재귀함수는 스택과 같이 작동하므로 사용하면 메모리 초과 및 recursion 에러가 날 수 있음
