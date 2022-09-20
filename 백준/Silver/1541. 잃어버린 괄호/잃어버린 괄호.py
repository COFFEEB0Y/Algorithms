# 잃어버린 괄호
"""
괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.
"""

# 55 - 50 + 40
# 55 - ( 50 + 40 ) = -35

# 40 - 60 + 70 + 70 - 40
# 40 - (60 + 70 + 70) - 40 = -200

import sys

s = sys.stdin.readline().rstrip().split(sep= '-')       # -를 기준으로 문자열 나누기

pos = s[0]      # s의 첫 번째 원소 빼고는 전부 음수가 됨
neg = []
for i in range(1,len(s)):
    neg.append(s[i])

pos = sum(map(int, (pos.split(sep='+'))))

neg_sum = 0

for ne in neg:
    neg_sum += sum(map(int, (ne.split(sep='+'))))

print(pos-neg_sum)