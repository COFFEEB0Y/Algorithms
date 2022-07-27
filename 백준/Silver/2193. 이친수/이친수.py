# 이친수(pinary number)
# N자리의 이친수의 개수를 출력

import sys

N = int(sys.stdin.readline())   # N자리

dp = [ [0, 0], [0 , 1], [1, 0] ]
if N >= 3:
    dp += [[0, 0] for i in range(N-2)]
    for j in range(3,N+1):
        dp[j][0] = dp[j-1][0] + dp[j-1][1]       # 0으로 끝나는 이친수의 경우 0, 1을 뒤에 붙일 수 있음
        dp[j][1] = dp[j-1][0]      # 1로 끝나는 이친수의 경우 뒤에 0밖에 못 붙임

print(sum(dp[N]))