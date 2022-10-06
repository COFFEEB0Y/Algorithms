# 보물

import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A = sorted(A)
B = sorted(B, reverse=True)

S = 0

for i in range(N):
    S += (A[i] * B[i])

print(S)