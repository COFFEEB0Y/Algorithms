import sys


def is_PrimeNumber(num):
    for i in range(2, int(num**0.5)+1):  # 2~(num-1)까지의 수 중 하나라도 나누어 떨어진다면 소수가 아님
        if num % i == 0:
            return False
    return True


while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        a, b = 3, n - 3  # b-a 의 차이가 가장 크게 하기 위해
        while a != b:
            if is_PrimeNumber(a) and is_PrimeNumber(b):
                print('%d = %d + %d' % (n, a, b))
                break
            else:
                a += 1
                b -= 1
            if a == b:
                print("Goldbach's conjecture is wrong.")
