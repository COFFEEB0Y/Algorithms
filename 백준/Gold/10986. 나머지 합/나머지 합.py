# 나머지 합

"""연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램"""

# 둘째 줄에 N개의 수 A1, A2, ..., AN이 주어진다. (0 ≤ Ai ≤ 10**9)
# 연속된 부분 구간의 합 -> 구간합 사용

"""
우리가 구하려고 하는 것 : sum(i,j) % M == 0을 만족하는 쌍 (i, j) 찾기
                      (sum(1, j) - sum(1, i-1)) % M == 0
                      sum(1,j) % M == sum(1, i-1) % M 을 만족하는 쌍 (i, j)찾기
        따라서) 1부터 N까지의 구간합 중 M으로 나눈 나머지가 같은 2개를 조합하면 된다  
"""


import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
# prefix_sum
prefix_sum = []
v = 0
for i in A:
    v += i
    prefix_sum.append(v)

# 구간합을 M으로 나눈 나머지를 저장하는 리스트 (M으로 나눈 나머지는 0부터 M-1까지 M개)
r = [0] * M

for a in prefix_sum:
    r[a % M] += 1
# 구간합을 M으로 나눈 나머지가 0인 경우는 당연히 나누어 떨어짐
# 구간합을 M으로 나눈 나머지가 같은 경우 중 2개 고르기 (조합)

ans = r[0]
for i in r:
    if i <= 1:
        continue
    ans += (i * (i-1)) / (2 * 1)

print(int(ans))



