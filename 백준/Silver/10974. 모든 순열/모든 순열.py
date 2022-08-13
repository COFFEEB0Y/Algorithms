# 모든 순열

import sys
from itertools import permutations
N = int(sys.stdin.readline())

its = list(permutations(range(1, N+1), N))

for i in its:
    print(*i)

