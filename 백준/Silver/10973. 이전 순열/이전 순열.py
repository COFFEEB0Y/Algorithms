# 이전 순열

import sys
N = int(sys.stdin.readline())

sequence = list(map(int, sys.stdin.readline().split()))

find = False

for i in range(N-1, 0, -1):
    if sequence[i] < sequence[i-1]: # 앞의 숫자가 뒤의 숫자보다 크면
        for j in range(N-1, -1, -1):
            if sequence[i-1] > sequence[j]:
                sequence[i-1], sequence[j] = sequence[j], sequence[i-1]
                new_sequence1 = sequence[:i]
                new_sequence2 = sorted(sequence[i:], reverse=True) # 내림차순으로 기준값 다음을 정
                sequence = new_sequence1 + new_sequence2
                find = True
                break
    if find:
        print(*sequence)
        break

if not find:
    print(-1)