# 수 이어쓰기 1
"""
1부터 N까지의 수를 이어서 쓰면 다음과 같이 새로운 하나의 수를 얻을 수 있다.
이렇게 만들어진 새로운 수는 몇 자리 수일까? 이 수의 자릿수를 구하는 프로그램을 작성하시오.
"""

# 시간초과 문제 -> Pypy에서는 통과 but Python3는 시간초과
# 숫자의 자릿수에는 규칙이 있음
import sys

N = sys.stdin.readline().rstrip()
count = 0
for i in range(1,len(N)):
    count += 9*10**(i-1)*i
count += (int(N)-10**(len(N)-1)+1)*len(N)
print(count)

