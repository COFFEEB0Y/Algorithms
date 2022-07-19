# 1,2,3 더하기 (다이나믹 프로그래밍 활용)
# 정수 n이 주어졌을 때, 1, 2, 3으로 나타내는 방법의 수 구하기
import sys

T = int(sys.stdin.readline()) # 테스트 케이스의 개수

dp = [0, 1, 2, 4] + [0] * 7  # 11 크기의 배열을 준비 (n이 최대 10까지 가능)
for i in range(4,11):        # 4~10까지 진행
    dp[i] = dp[i-1] + dp[i-2] +dp[i-3]  # 5의 결과 = 4+1, 3+2, 2+1 (1+4는 뒤에 4를 추가할 수 없기 때문에 불가능)

for _ in range(T):
    n = int(sys.stdin.readline())       # n은 양수이며 11보다 작다는 조건이 있다
    print(dp[n])
