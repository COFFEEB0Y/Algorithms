# 참외밭

import sys
K = int(sys.stdin.readline())  # 1m2의 넓이에 자라는 참외의 개수

sides = [list(map(int, sys.stdin.readline().split())) for _ in range(6)]

w, w_idx = 0, 0    # 가장 길이가 긴 가로변의 길이와 인덱스
h, h_idx = 0, 0

for i in range(len(sides)):
    if sides[i][0] == 1 or sides[i][0] == 2:
        if w < sides[i][1]:
            w = sides[i][1]
            w_idx = i
    elif sides[i][0] == 3 or sides[i][0] == 4:
        if h < sides[i][1]:
            h = sides[i][1]
            h_idx = i

# 가장 긴 변의 양 옆 변을 빼서 가장 작은 변의 길이를 구함

s_h = abs(sides[(h_idx - 1) % 6][1] - sides[(h_idx + 1) % 6][1])
s_w = abs(sides[(w_idx - 1) % 6][1] - sides[(w_idx + 1) % 6][1])

area = (w * h) - (s_w * s_h)

print(K * area)