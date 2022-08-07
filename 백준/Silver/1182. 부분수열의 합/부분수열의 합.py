import sys
from itertools import combinations
N, S = map(int, sys.stdin.readline().split())

sequence = list(map(int, sys.stdin.readline().split()))

# 연속된 부분수열이 아님!! -> 조합을 사용하여 모든 부분수열을 구함

count = 0       # 합이 S를 만족하는 부분수열의 개수

com = []
for i in range(1,N+1):
    com += list(combinations(sequence, i))      # 리스트 간 서로 더할 수 있음

for i in range(len(com)):
    if sum(com[i]) == S:
        count += 1

print(count)







