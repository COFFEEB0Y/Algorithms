"""
ROT13 -> 알파벳의 개수 26 : 아스키 코드의 차이가 13씩 나는 것끼리 묶음
"""

import sys

string = sys.stdin.readline().rstrip()
ans = []
for c in string:
    if c.isupper():
        if 65 <= ord(c) <= 77:    # A~M
            ans.append(chr(ord(c)+13))
        else:
            ans.append(chr(ord(c)-13))
    elif c.islower():
        if 97 <= ord(c) <= 109:  # a~m
            ans.append(chr(ord(c) + 13))
        else:                    # n~z
            ans.append(chr(ord(c) - 13))
    else:       # 대문자, 소문자 이외에는 ROT13을 적용하지 않음 -> 공백이나 숫지는 그대로 다시 문자열에
        ans.append(c)

print(''.join(ans))