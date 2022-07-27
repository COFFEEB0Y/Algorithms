# 직각삼가형 판별 문제
# (가장 긴 변의 길이) ** 2 == 나머지 두 변의 길이의 제곱의 합


import sys

while True:
    s1, s2, s3 = sys.stdin.readline().split()
    s1 = int(s1)
    s2 = int(s2)
    s3 = int(s3)
    if s1 == 0 and s2 == 0 and s3 == 0:
        break
    longest_s = max(s1, s2, s3) # 가장 긴 변의 길이 찾기
    if s1 == longest_s:
        if s1 ** 2 == (s2 ** 2) + (s3 ** 2):
            print('right')
        else:
            print('wrong')
    elif s2 == longest_s:
        if s2 ** 2 == (s1 ** 2) + (s3 ** 2):
            print('right')
        else:
            print('wrong')
    elif s3 == longest_s:
        if s3 ** 2 == (s2 ** 2) + (s1 ** 2):
            print('right')
        else:
            print('wrong')
