import sys
from itertools import  combinations
N, M = map(int, sys.stdin.readline().split())
lst = sorted(list(map(int, sys.stdin.readline().split())))

# itertools 라이브러리로 풀기
lst = sorted((set(combinations(lst, M))))

for i in lst:
    print(*i)


