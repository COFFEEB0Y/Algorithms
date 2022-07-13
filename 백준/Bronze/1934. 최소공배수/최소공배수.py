import sys


def gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


def lcm(num1, num2):
    return (num1 * num2) / gcd(num1, num2)  # 두 수의 곱에 최대공약수를 나누면 최소공배수가 나온다


ans = []
T = int(sys.stdin.readline())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    ans.append(lcm(a, b))

for i in range(len(ans)):
    print(round(ans[i]))
