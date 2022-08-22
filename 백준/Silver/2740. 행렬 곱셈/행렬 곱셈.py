# 행렬 곱셈

import sys

A = []
B = []
# 행렬A 생성
N, M = map(int, sys.stdin.readline().split())
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))
# 행렬B 생성
M, K = map(int, sys.stdin.readline().split())
for _ in range(M):      # 왼쪽 행렬의 열과 오른쪽 행렬의 행의 수가 일치해야 함
    B.append(list(map(int, sys.stdin.readline().split())))

ans = 0
# 행렬 A 곱하기 행렬 B
for i in range(N):
    for k in range(K):
        for j in range(M):
            ans += A[i][j]*B[j][k]
        print(ans, end=' ')
        ans = 0
    print()


