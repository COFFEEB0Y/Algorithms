# 카드

"""
준규가 가지고 있는 카드가 주어졌을 때, 가장 많이 가지고 있는 정수를 구하는 프로그램을 작성하시오.
만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.
"""

import sys

N = int(sys.stdin.readline())

num_dict = {}

for _ in range(N):
    num = int(input())
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1
# 카드의 개수를 기준으로 내림차순 -> 카드의 개수가 같다면 카드 숫자의 값을 기준으로 오름차순
dic = sorted(num_dict.items(), key=lambda x: (-x[1], x[0])) 
print(dic[0][0])