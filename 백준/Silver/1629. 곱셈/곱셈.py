# 곱셈

"""자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오."""

import sys

A, B, C = map(int, sys.stdin.readline().split())
# A, B, C는 모두 2,147,483,647 이하의 자연수이다.

# 그냥 A를 B번 제곱해주게 되면 시간이 너무 오래 걸린다
# 분할 정복을 이용한 거듭제곱
# 나머지 분배 법칙에 대한 이해

def recursive_power(C, n, m):
    if n == 1:
        return C % m
    if n % 2 == 0:
        a = recursive_power(C, n//2, m)
        return ((a % m)*(a % m)) % m
    else:
        a = recursive_power(C, (n-1)//2, m)
        return ((a % m)*(a % m)*(C % m)) % m

print(recursive_power(A, B, C))