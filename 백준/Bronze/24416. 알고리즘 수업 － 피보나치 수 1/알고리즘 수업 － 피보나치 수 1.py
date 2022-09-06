# 알고리즘 수업 - 피보나치 수 1
"""n의 피보나치 수를 구할 경우 코드1 코드2 실행 횟수를 출력하자."""
import sys

N = int(sys.stdin.readline())

count_fibo = 0
count_fibonacci = 0

def fibo(n):
    global count_fibo
    if n==1 or n==2:
        count_fibo += 1
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def fibonacci(n):
    global count_fibonacci
    lst = [0] * (n+1)
    lst[1] = 1
    lst[2] = 1
    for i in range(3, n+1):
        count_fibonacci += 1
        lst[i] = lst[i-1] + lst[i-2]
    return lst[n]

fibo(N)
fibonacci(N)
print(count_fibo)
print(count_fibonacci)
