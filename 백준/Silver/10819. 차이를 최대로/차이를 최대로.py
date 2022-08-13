# 차이를 최대로

# 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|


import sys
from itertools import permutations
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
As = list(permutations(A,N))
result = []
for i in As:
    v = 0
    for j in range(len(i)-1):
        v += abs(i[j] - i[j+1])
    result.append(v)

print(max(result))
