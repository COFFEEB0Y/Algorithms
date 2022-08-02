"""
검문 문제
유클리드 호제법 사용하지 않고 풀기
"""

def gcd_several(array): # 여러 수의 최대공약수를 구하는 함수
    V = array[0]
    for i in range(1, len(array)):
        V = math.gcd(V, array[i])
    return V


def divisor(num):   # 어떤 수의 약수 구하기
    divisors = []
    for i in range(1,int(num**0.5)+1):      # 약수는 대칭관계를 가지고 있음
        if num % i == 0:
            divisors.append(i)
            divisors.append(num // i)
    divisors = list(set(divisors))
    divisors.sort()
    divisors.remove(1)
    print(*divisors)



import sys
import math

N = int(sys.stdin.readline())   # 종이에 적은 수의 개수
Ms = [] # M들이 저장되는 리스트
Ns = [int(sys.stdin.readline()) for _ in range(N)] # 종이에 적은 숫자들의 종류
Ns.sort()   # 적은 숫자들을 오름차순으로 배열


new_Ns = [(Ns[i]-Ns[i-1]) for i in range(1,N)]  # 유클리드 호제법 사용
divisor(gcd_several(new_Ns))    # 1을 제외한 최대공약수의 약수들
