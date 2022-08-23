# Matrix Multiplication Calculator

import sys


# 행렬곱 함수
def mul_matrix(input_matrix, square_matrix, M, N, P, Q):

    # 새로 만들어진 행렬을 저장할 변수 C
    C = [[0 for _ in range(Q)] for _ in range(M)]

    for i in range(M):  # 왼쪽 행렬의 행
        for k in range(Q):  # 오른쪽 행렬의 열
            for j in range(N):  # 왼쪽 행렬의 열 = 오른쪽 행렬의 행 (행렬의 곱 조건)
                C[i][k] += input_matrix[i][j]*square_matrix[j][k]

    return C    # 곱해진 행렬을 반환


case = 1

while True:
    M, N, P, Q = map(int, sys.stdin.readline().split())

    if M == 0 and N == 0 and P == 0 and Q == 0:
        break

    m1 = []         # 왼쪽 행렬
    m2 = []         # 오른쪽 행렬

    for _ in range(M):
        m1.append(list(map(int, sys.stdin.readline().split())))

    for _ in range(P):
        m2.append(list(map(int, sys.stdin.readline().split())))

    if N != P:  # 행렬곱이 성립하지 않는 경우
        print("Case #%d:" % case)
        print("undefined")

    else:
        new_matrix = mul_matrix(m1, m2, M, N, P, Q) # 곱해진 행렬을 new_matrix로 받음
        print("Case #%d:" % case)
        for i in new_matrix:
            print("|", end=' ')
            for j in i:
                print(j, end=' ')
            print("|")

    case += 1