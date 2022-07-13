"""
각가의 테스트 케이스마다 골드바흐 파티션의 개수를 출력한다 (두 소수의 순서만 다른 것은 같은 파티션이다)
"""

import sys

arr = [False, False] + [True for i in range(999999)]    # 에라토스테네스의 체 사용

for i in range(2, int(1000000**0.5)+1):
    if arr[i]:
        j = 2
        while i * j <= 1000000:
            arr[i*j] = False
            j += 1


T = int(sys.stdin.readline())
for _ in range(T):
    num = int(sys.stdin.readline())
    count = 0
    for i in range(1, int(num/2)+1):
        if arr[i] and arr[num-i]:
            count += 1

    print(count)
