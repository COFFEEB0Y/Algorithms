import sys
input = sys.stdin.readline
X = int(input())    # 계산한 총 금액
N = int(input())

total_price = 0
for _ in range(N):
    price, number = map(int, input().split())
    total_price += price * number

if X == total_price:    # 영수증의 적힌 금액과 계산한 총 금액이 맞다면
    print('Yes')
else:
    print('No')