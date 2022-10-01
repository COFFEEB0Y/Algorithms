import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = sorted(A)

P = [0] * N     # 배열 A의 각 원소에 적용되는 배열 P의 각 원소

for i in range(N):
    P[i] = B.index(A[i])
    B[P[i]] = -1

print(*P)

