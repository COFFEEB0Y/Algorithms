"""
다각형의 면적 구하기 문제
N이 4이상이 다각형을 N-2개의 삼각형으로 쪼개어 생각
세 점의 좌표를 알고 있다면 삼각형의 넓이를 구할 수 있음
"""

import sys

N = int(sys.stdin.readline()) # N개의 점으로 이루어진 다각형

dots = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # N개의 점들의 좌표들이 주어짐

xs = [i[0] for i in dots]   # x좌표들을 나열
ys = [i[1] for i in dots]   # y좌표들을 나열

def polygon_area(xs, ys): # N 다각형의 넓이 구하는 공식 (사선 공식)
    xs = xs + [xs[0]]
    ys = ys + [ys[0]]
    start = 0
    end = 0
    for i in range(N):
        start += xs[i] * ys[i+1]
        end += ys[i] * xs[i+1]
    re = abs(start - end)
    return round((re * 0.5), 1)

# 만약 원점 기준으로 모서리들이 반시계 방향으로 돈다면 양의 면적이 더해지게 되고 / 반시계 방향으로 돈다면 음의 면적이 더해지게 되는 것이다

print(polygon_area(xs, ys))