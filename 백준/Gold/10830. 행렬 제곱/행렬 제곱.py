# 행렬 제곱

"""크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오"""

import sys

A = []

# 행렬A 생성 (A는 정방행렬 -> size만 입력)
N, B = map(int, sys.stdin.readline().split())
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

# 행렬곱 함수
def square_matrix(input_matrix, square_matrix):

    # 새로 만들어진 행렬을 저장할 변수 output_matrix
    output_matrix = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):  # 왼쪽 행렬의 행
        for k in range(N):  # 오른쪽 행렬의 열
            for j in range(N):  # 왼쪽 행렬의 열 = 오른쪽 행렬의 행 (행렬의 곱 조건)
                output_matrix[i][k] += input_matrix[i][j]*square_matrix[j][k]
                output_matrix[i][k] %= 1000
    return output_matrix    # 곱해진 행렬을 반환

# 행렬 제곱 함수 (행렬곱 함수를 이용)
# 분할 정복을 이용한 거듭제곱
def recursive_square_matrix(input_matrix_r, n):  # 입력 행렬의 제곱이기 떄문에 인자로 입력 행렬 하나만을 받는다

    if n == 1:
        return input_matrix_r

    if n % 2 == 0:
        a = recursive_square_matrix(input_matrix_r, n // 2)
        return square_matrix(a, a)

    else:
        a = recursive_square_matrix(input_matrix_r, (n-1) // 2)
        return square_matrix(square_matrix(a, a), input_matrix_r)


ans_matrix = recursive_square_matrix(A, B)  # 행렬 A를 B제곱해서 나온 행렬

for i in ans_matrix:
    for j in i:
        print(j % 1000, end=' ')
    print()


