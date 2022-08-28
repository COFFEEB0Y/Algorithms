# 링
""" 첫 번째 링을 한 바퀴 돌리면 그 링은 몇 바퀴 도는지 기약 분수 형태 A/B로 출력한다."""
import sys


def gcd(a, b):
    if a % b == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)


N = int(sys.stdin.readline())

rings = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    gcd_num = gcd(rings[0], rings[i])
    print("%d/%d" % (rings[0] // gcd_num, rings[i] // gcd_num))

