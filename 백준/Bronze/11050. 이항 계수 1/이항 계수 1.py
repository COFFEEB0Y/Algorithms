# 이항계수1
"""자연수N과 자연수K가 주어졌을 때 이항계수 (N,K)를 구하시오"""

import sys
from itertools import combinations
N, K = map(int, sys.stdin.readline().split())

com = list(combinations(range(N), K))
print(len(com))

