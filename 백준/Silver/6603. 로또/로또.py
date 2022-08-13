# 로또

import sys
from itertools import combinations

while True:
    lst = list(map(int, sys.stdin.readline().split()))
    if len(lst) == 1:
        break
    lst = lst[1:]
    coms = list(combinations(lst,6))
    for com in coms:
        print(*com)
    print()

