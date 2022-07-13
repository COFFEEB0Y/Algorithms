import sys

A, B, C, D = map(int, sys.stdin.readline().split())

A_B = int(str(A)+str(B))
C_D = int(str(C)+str(D))

print(A_B + C_D)
