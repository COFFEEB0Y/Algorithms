"""
1을 N제곱한 일의 자리수 -> 1
2 -> 2, 4, 8, 6, 2, 4, 8,
3 -> 3, 9, 7, 1, 3, 9
4 -> 4 6 4 6
5 -> 5 5 5 5
6 -> 6 6 6 6
7 -> 7 9 3 1 7 9 3 1
8 -> 8 4 2 6 8 4 2 6
9 -> 9 1 9 1
0 -> 0 0 0 0
"""

import sys

num_dict = {9: [9, 1], 4: [4, 6], 2: [2, 4, 8, 6], 3: [3, 9, 7, 1], 7: [7, 9, 3, 1], 8: [8, 4, 2, 6]}

T = int(sys.stdin.readline())

# 일의 자리는 계속 반복된다는 점을 이용

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    a = a % 10  # 그 숫자의 일의 자리
    if a == 0:
        print(10)
        continue
    elif a == 5 or a == 6 or a == 1:
        print(a)
        continue
    else:  # 일의 자리가 2, 3, 4, 7, 8, 9인 수
        x = b % len(num_dict[a])
        print(num_dict[a][x-1])
