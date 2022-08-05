from itertools import permutations
import sys

N, M = map(int, sys.stdin.readline().split())   # 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

it = list(permutations(range(1,N+1), M))    # 순열 (중복없이 M개를 고르는 수열) -> 순서가 있음

for i in it:
    print(*i)

