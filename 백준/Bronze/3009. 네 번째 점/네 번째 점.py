# 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램

import sys

x = []  # x좌표들의 리스트
y = []  # y좌표들의 리스트

# 세 점의 좌표가 주어진다

for _ in range(3):
    a, b = map(int, sys.stdin.readline().split())
    x.append(a)
    y.append(b)

for i in range(3):          # 직사각형의 점들은 같은 x좌표와 y좌표를 2개씩 
    if x.count(x[i]) == 1:  
        x4 = x[i]           # 4번째 점의 x죄표
    if y.count(y[i]) == 1:
        y4 = y[i]           # 4번째 점의 y좌표

print(x4, y4)