# 터렛

"""
마린이 있을 수 있는 좌표의 수를 출력
두 원의 관걔
"""

import sys

for _ in range(int(sys.stdin.readline())):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    b_r = max(r1, r2)
    s_r = min(r1, r2)
    # 두 터렛 사이의 거리
    distance = ((abs(x1 - x2)**2 + abs(y1-y2)**2)) ** 0.5
    # 두 터렛 사이의 거리가 0인 경우
    if distance == 0:
        if r1 == r2: # 만나는 점의 개수가 무한인 경우
            print(-1)
            continue
        else:   # 만나는 점이 아예 없는 경우
            print(0)
            continue

    else:
        if distance < r1 + r2:
            if b_r - s_r > distance:
                print(0)
                continue
            elif b_r - s_r < distance:
                print(2)
                continue
            else:
                print(1)
                continue

        elif distance == r1 + r2:  # 외접하는 경우
            print(1)
            continue

        else:
            print(0)


