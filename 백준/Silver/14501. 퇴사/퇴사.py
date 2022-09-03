# 퇴사

"""상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오."""

'''둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며, 1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)'''

# 맨 마지막부터 올 수 있는 값으로 넣어주기
import sys

N = int(sys.stdin.readline())

time = []
pay = []
dp = []
for i in range(N):
    a, b = map(int, input().split())
    time.append(a)
    pay.append(b)
    dp.append(b)
dp.append(0)
for i in range(N - 1, -1, -1):
    if time[i] + i > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], pay[i] + dp[i + time[i]])
print(dp[0])

