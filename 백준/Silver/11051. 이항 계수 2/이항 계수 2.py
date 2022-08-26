# 이항계수2
"""자연수N과 자연수K가 주어졌을 때 이항계수 (N,K)를 10007로 나눈 나머지를 구하시오"""

import sys
N, K = map(int, sys.stdin.readline().split())

up = 1
down = 1
for i in range(N, N-K, -1):
    up *= i
for j in range(1,K+1):
    down *= j
binomial_coefficient = up // down
print(binomial_coefficient % 10007)