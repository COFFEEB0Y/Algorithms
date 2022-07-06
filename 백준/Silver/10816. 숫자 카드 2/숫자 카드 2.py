import sys
from collections import Counter

N = int(sys.stdin.readline())
while True:
    num_list = list(map(int, sys.stdin.readline().split()))
    if len(num_list) == N:
        break
counter = Counter(num_list)
M = int(sys.stdin.readline())
ans = []
while True:
    num_list2 = list(map(int, sys.stdin.readline().split()))
    if len(num_list2) == M:
        break
for num in num_list2:
    if num in counter.keys():
        ans.append(counter[num])
    else:
        ans.append(0)
for i in ans:
    print(i, end=' ')
