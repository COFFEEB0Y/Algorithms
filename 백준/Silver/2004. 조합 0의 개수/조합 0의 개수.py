import sys

def countNum(N, num):
    count = 0
    while N != 0:     # 그 수로 더 이상 나누어 떨어지지 않을 떄까지 나눈다
        N = N // num
        count += N
    return count


n, m = map(int, sys.stdin.readline().split())   # 2와 5의 쌍의 개수를 구하면 끝자리 0의 개수를 알 수 있다
count_2 = countNum(n, 2) - countNum(m, 2) - countNum(n-m, 2)
count_5 = countNum(n, 5) - countNum(m, 5) - countNum(n-m, 5)
print(min(count_2, count_5))


