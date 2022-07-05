# 동전 문제 (그리디 알고리즘)
# K원을 만드는 데 필요한 최소한의 동전 개수를 구하여라.
import sys
N, K = map(int, sys.stdin.readline().split())
coins = []      # 동전들의 가치들
for _ in range(N):
    coin = int(sys.stdin.readline().rstrip())
    coins.append(coin)
coins.sort(reverse= True)   # 동전들을 가치가 큰 것부터 작은 것 순으로 나열
count = 0                   # 동전의 개수
for i in coins:
    if K == 0:
        break
    if K // i >= 1:         # 주어진 값과 동전을 나누어 몫이 1이상이면 
        count += K // i     # count 갱신
        K = K % i           # 주어진 값을 최신화
print(count)


