import sys

n = int(sys.stdin.readline())

dp = [0] * 1001

dp[1] = 1  # 2X1 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수는 1가지
dp[2] = 3

for i in range(3, 1001):
    dp[i] = dp[i - 1] + (2 * dp[i - 2])

print(dp[n] % 10007)
