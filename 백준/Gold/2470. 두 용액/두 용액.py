# 두 용액 문제
# 투 포인터 알고리즘
# 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액의 특성값을 출력

import sys

N  = int(sys.stdin.readline())
fs = list(map(int, sys.stdin.readline().split()))

e = N-1      # 합이 양수일 때 왼쪽으로
s = 0  # 합이 음수일 때 오른쪽으로

f1 = 0
f2 = 0

nearest_zero = 1999999999

fs.sort()

if fs[N-1] <= 0: # 용액이 전부 염기성
    f1 = fs[N-2]
    f2 = fs[N-1]

elif fs[0] >= 0:    # 가장 작은 수가 양수 -> 전부 다 양수 (산성)
    f1 = fs[0]
    f2 = fs[1]

else:       # 산성 용액과 염기성 용액이 섞여있는 경우
    while s < e:
        sum = fs[s] + fs[e] # 두 용액의 합
        zero = abs(sum)  # 0에 얼마나 가까운지 나타내는 지표
        if nearest_zero > zero:
            f1 = fs[s]
            f2 = fs[e]
            nearest_zero = zero

        if sum < 0:
            s += 1

        else:
            e -= 1

print(f1, f2)


