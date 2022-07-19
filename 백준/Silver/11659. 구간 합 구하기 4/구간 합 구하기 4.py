# 구간합 구하기

import sys

N, M = map(int, sys.stdin.readline().split()) # 수의 개수 N, 합을 구해야 하는 횟수 M
sum_list = []    # i부터 j까지의 합을 구한 값들을 저장하는 리스트

num_list = [0] + list(map(int, sys.stdin.readline().split()))   # 인덱스를 맞추기 위해

sum = 0
for i in range(len(num_list)):
    sum += num_list[i]
    num_list[i] = sum


for _ in range(M):     # num_list[j] - num_list[i-1]
    i, j = map(int, sys.stdin.readline().split())
    sum_list.append(num_list[j]-num_list[i-1])

for i in sum_list:
    print(i)
