import sys
from itertools import combinations

N = int(sys.stdin.readline())


fs = list(map(int, sys.stdin.readline().split()))

pairs = list(combinations(fs, 2))

difference_zero = []

for i in range(len(pairs)):
    difference_zero.append(abs(0-sum(pairs[i])))

a, b = pairs[(difference_zero.index(min(difference_zero)))]

print(a, b)

