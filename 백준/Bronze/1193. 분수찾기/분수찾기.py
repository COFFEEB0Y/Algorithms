# 단계 + 1 =  분모 + 분자
# 1 -> 1단계  2,3 -> 2단계 4,5,6 -> 3단계 (n 단계마다 n 개의 원소를 가진다)
# ex) X = 4라면 -> 3단계 1번째 원소

import sys

X = int(sys.stdin.readline())


lv = 1
s = 1
while X - s > 0:
    lv += 1
    s += lv

s -= lv
num = X - s

# 분자와 분모의 합은 단계 + 1
sum_u_d = lv + 1

# 몇 번째 원소인지는 단계가 홀수냐 짝수냐에 따라 다름 (짝수라면 위에서 아래로, 홀수라면 아래에서 위로)
if lv % 2 == 0:
    print("%d/%d" % (num, sum_u_d - num))
else:
    print("%d/%d" % (sum_u_d - num, num))
