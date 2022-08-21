# 피보나치 함수

"""N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오."""

# 0 <= N <= 40

import sys


def fibo(n):
    global ans
    ans = [0, 0]

    if dp[n] != -1:
        return dp[n]

    if n == 1:
        ans[1] += 1
        dp[n] = [ans[0], ans[1]]
        return [ans[0], ans[1]]
    elif n == 0:
        ans[0] += 1
        dp[n] = [ans[0], ans[1]]
        return [ans[0], ans[1]]
    else:
        dp[n] = [fibo(n-1)[0] + fibo(n-2)[0], fibo(n-1)[1] + fibo(n-2)[1]]
        return dp[n]
        # fibonacci(0)와 fibonacci(1)이 몇 번 호출되는지

T = int(sys.stdin.readline())

ans = [0, 0]

dp = [-1] * 41  # N의 범위가 0에서 40까지

for _ in range(T):
    N = int(sys.stdin.readline())
    print(*fibo(N))



