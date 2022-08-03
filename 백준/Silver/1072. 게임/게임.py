import sys
import math


X, Y = map(int, sys.stdin.readline().split()) # X는 게임 횟수, Y는 이긴 횟수

# 게임은 무조건 이기기 때문에 Y가 1씩 증가 but 게임 횟수 또한 1씩 증가

Z = math.trunc(100 * Y/X) # 기존의 Z

start = 1   # 게임의 최소 횟수
end = X     # 게임의 최대 횟수
result = -1 # 만약 Z가 절대 변하지 않는다면 -1을 출력한다. -> result를 -1로 초기화 후 다른 값으로 갱신
while start <= end:
    mid = (start + end) // 2    # 게임의 횟수 mid
    c = math.trunc(100 * (Y+mid)/(X+mid))     # 승률 갱신
    if c >= Z+1: # 횟수를 줄어야 함
        result = mid    # 조건을 만족하는 횟수(mid)를 result변수에 넣어준다
        end = mid-1
    else: # 아직 기준치를 만족하지 못함 -> 횟수를 늘려야함
        start = mid + 1

print(result)





