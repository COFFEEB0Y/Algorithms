# itertools 라이브러리러 풀기

import sys
from itertools import product
N, M = map(int, sys.stdin.readline().split())

it = list(product(range(1,N+1), repeat= M))

for i in it:
    print(*i)
