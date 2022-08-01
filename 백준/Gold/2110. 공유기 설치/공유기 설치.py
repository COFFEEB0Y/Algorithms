# 공유기 문제

import sys

N, C = map(int, sys.stdin.readline().split()) # 집의 개수 N, 공유기의 개수 C

house_x = [int(sys.stdin.readline()) for _ in range(N)] # 수직선 위에 있는 집들의 위치
house_x.sort()

start = 1   # 공유기간의 거리 최솟값 1
end = house_x[-1] - house_x[0]  # 공유기간의 거리 최댓값

while start <= end:
    mid = (start + end) // 2
    current_house = house_x[0]  # 첫 번째 집에 먼저 공유기를 달고 시작
    count = 1 # 설치한 공유기의 개수
    for i in house_x:
        if i >= mid + current_house:
            count += 1
            current_house = i
    if count >= C:  # 설치된 공유기의 개수가 설치해야될 공유기의 개수 보다 많다 -> 공유기 간의 거리 늘리기
        result = mid
        start = mid + 1
    else:    # 공유기를 더 많이 설치해야 함 -> 공유기 간의 거리 줄이기
        end = mid -1

print(result)