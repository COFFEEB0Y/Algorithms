import sys
input = sys.stdin.readline

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:   # 문제에서의 종료 조건
        break

    if A % B == 0:  # 첫 번째 숫자가 두 번쨰 숫자에 의해 나누어 떨어진다면
        print('multiple')

    elif B % A == 0:
        print('factor')

    else:
        print('neither')



