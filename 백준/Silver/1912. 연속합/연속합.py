# 연속합
"""
n개의 정수로 이루어진 임의의 수열이 주어진다.
우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다
"""

# 다이내믹 프로그래밍

import sys

n = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().strip().split()))

interval_sum = [num_list[0]]     # 연속합들을 저장하는 리스트

# interval_sum[i] + num_list[i+1] 과 num_list[i+1]를 비교해서 큰 값을 선택
# 지금까지의 합과 현재 수를 더하는 것 vs 현재 수만을 선택하는 것
for i in range(len(num_list)-1):
    interval_sum.append(max(interval_sum[i] + num_list[i+1], num_list[i+1]))

print(max(interval_sum))