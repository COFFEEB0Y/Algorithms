# 카드 팩의 가격이 주어졌을 때. N개의 카드를 구매하기 위해 민규가 지불해야 하는 금액의 최댓값을 구하는 프로그램
# 구매한 카드팩에 포함된 카드 개수의 합은 N과 같아야 한다

import sys

N = int(sys.stdin.readline())   # 민규가 구매해야 하는 카드의 개수 N

while True:
    Ps = list(map(int, sys.stdin.readline().split()))  # 만약에 N이 4라면 P1~P4까지
    if len(Ps) == N:
        break

dp = [0] + Ps       # 카드 0장을 뽑는 가지수는 0개 , index를 맞추기 위해 추가

for i in range(1, N+1):
    for k in range(1, i+1):
        dp[i] = max(dp[i], dp[k] + dp[i-k])         # dp[4] = max(dp[4], dp[3]+dp[1], dp[2]+dp[2], dp[1]+dp[3]) 

print(dp[N])

