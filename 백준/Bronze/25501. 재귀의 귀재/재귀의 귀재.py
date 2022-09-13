# 재귀의 귀재

"""
문자열 $S$를 isPalindrome 함수의 인자로 전달하여 팰린드롬 여부를 반환값으로 알아낼 것이다.
더불어 판별하는 과정에서 recursion 함수를 몇 번 호출하는지 셀 것이다.
"""

# 각 테스트케이스마다, isPalindrome 함수의 반환값과 recursion 함수의 호출 횟수

import sys


def recursion(s, l, r):
    global count
    count += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)


def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


count = 0 # recursion함수의 호출 횟수

N = int(sys.stdin.readline())

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    print(isPalindrome(word), count)
    count = 0  # recursion 함수의 호출 횟수를 초기화

