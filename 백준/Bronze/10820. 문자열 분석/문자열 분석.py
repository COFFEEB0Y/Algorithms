import sys

while True:
    line = list(sys.stdin.readline().rstrip('\n'))

    if not line:
        break

    # 소문자, 대문자, 숫자, 공백
    low, up, num, space = 0, 0, 0, 0
    for each in line:
        if each.islower():
            low += 1
        elif each.isupper():
            up += 1
        elif each.isdigit():
            num += 1
        elif each.isspace():
            space += 1

    print(low, up, num, space)