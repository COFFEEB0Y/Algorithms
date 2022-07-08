import sys

T = int(sys.stdin.readline())
for _ in range(T):
    strings = sys.stdin.readline().strip().split()
    for string in strings:
        if string != strings[-1]:
            string = ''.join(reversed(string))  # reversed 사용시 iterator를 반환 -> join으로 다시 하나의 문자열로 변환
            print(string, end=' ')
        else:
            string = ''.join(reversed(string))
            print(string)


