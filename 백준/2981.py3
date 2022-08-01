"""
검문 문제
"""

import sys

N = int(sys.stdin.readline())   # 종이에 적은 수의 개수
Ms = [] # M들이 저장되는 리스트
Ns = [int(sys.stdin.readline()) for _ in range(N)] # 종이에 적은 숫자들의 종류
remainder_Ns = [0 for _ in range(min(Ns)+1)] # 나올 수 있는 나머지의 개수 : Ns에서 최솟값이 7이라면 0~6까지의 나머지가 생성될 수 있음
for i in range(2, min(Ns)+1):
    for j in Ns:
        remainder_Ns[j%i] += 1
    if N in remainder_Ns:
        Ms.append(i)
    for j in Ns:
        remainder_Ns[j%i] -= 1

print(*Ms)
