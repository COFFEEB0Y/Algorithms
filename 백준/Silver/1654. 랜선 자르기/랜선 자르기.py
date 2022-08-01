# 랜선짜르기 문제

import sys

K, N = map(int, sys.stdin.readline().split())   # 가지고 있는 랜선의 개수 K, 필요한 랜선의 개수 N

My_lan = [int(sys.stdin.readline()) for _ in range(K)]  # 가지고 있는 랜선의 길이들


start = 1
end = max(My_lan) # 하나의 랜선의 길이는 최소: 1 , 최대: 가지고 있는 랜선들 중 가장 긴 랜선의 길이

while start <= end:
    mid = (start + end) // 2
    lans = 0  # 잘린 랜선들의 개수
    for i in My_lan:
        lans += i // mid
    if lans >= N:   # 기준이 되는 랜선의 길이가 더 길어야 함
        start = mid +1
    else:       # 만들어진 랜선들의 개수가 기준 개수보다 적다면 기준이 되는 랜선의 길이가 줄어야 함
        end = mid -1

print(end)  # end 값으로 나누나



