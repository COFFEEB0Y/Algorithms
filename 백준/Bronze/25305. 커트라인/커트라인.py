# 커트라인

"""
커트라인이란 상을 받는 사람들 중 점수가 가장 가장 낮은 사람의 점수를 말한다
"""

import sys

N, k = map(int, sys.stdin.readline().split()) # 응시자의 수와 상을 받는 사람의 수

while True:
    scores = list(map(int, sys.stdin.readline().split()))
    if len(scores) == N:
        break

scores.sort(reverse=True)
print(scores[k-1])
