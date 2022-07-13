import sys


def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result


N = int(sys.stdin.readline())
count = 0   # 0이 아닌 숫자가 나올 때까지의 0의 개수

num = list(str(factorial(N))[::-1])

for i in range(len(num)):
    if num[i] == '0':
        count += 1
    else:
        break
print(count)