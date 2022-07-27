# 두 수의 합
# Two pointer algorithm

import sys
input = sys.stdin.readline

n = int(input())    # 수열의 크기
num_list = list(map(int, input().split()))  # 수열에 포함되는 수 (서로 다른 양의 정수)
x = int(input())

start = 0
end = n-1

count = 0 # x = ai + aj 를 만족하는 (ai,aj)쌍의 개수

num_list.sort() # 수열을 오름차순으로 정렬 < 서로 다른 n 개의 양의 정수가 들어있기 때문에 >

while start < end:
    if num_list[start] + num_list[end] == x:    # 두 수의 합이 x일 때
        start += 1
        end -= 1
        count += 1

    elif num_list[start] + num_list[end] < x:   # 두 수의 합이 x보다 작을 때
        start += 1

    elif num_list[start] + num_list[end] > x:      # 두 수의 합이 x보다 클 때
        end -= 1

print(count)


