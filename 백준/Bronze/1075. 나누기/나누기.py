# 나누기
"""
지민이는 정수 N의 가장 뒤 두 자리를 적절히 바꿔서 N을 F로 나누어 떨어지게 만들려고 한다.
만약 가능한 것이 여러 가지이면, 뒤 두 자리를 가능하면 작게 만들려고 한다.
"""

import sys
input = sys.stdin.readline

N = int(input())
F = int(input())

# 뒤의 두 자리를 00부터 시작해서 가장 처음으로 나누어 떨어지는 숫자까지

N = int(str(N)[:-2] + '00') # N을 뒤에 2자리가 00의 되게 초기화

while True:
    if N % F == 0:
        break
    N += 1

print(str(N)[-2:])  # 마지막 두 자리를 출력