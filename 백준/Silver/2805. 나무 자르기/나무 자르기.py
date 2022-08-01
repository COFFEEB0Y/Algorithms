# 나무 자르기 문제

import sys

N, M = map(int, sys.stdin.readline().split())   # 나무의 수 N, 집으로 가져가려고 하는 나무의 길이 M

trees = list(map(int, sys.stdin.readline().split())) # 나무들의 크기



start = 0
end = max(trees)    # 나무 절단기의 높이는 H ( 0 <= H <= max(trees) )

while start <= end:
    mid = (start + end) // 2        # mid 가 나무 절단기의 높이를 가르킴
    remaining_tree = 0  # 절단기로 자르고 남은 나무들의 길이의 합
    for i in trees:
        if i > mid:     # 절단기의 높이보다 나무가 높다면 자를 수 있음
            remaining_tree += i - mid
        if remaining_tree >= M:     # 시간초과 발생 방지 -> 잘려진 나무들의 길이의 합이 이미 적어도 M만큼 있다면 더 반복문을 돌릴 이유가 없다
            break
    if remaining_tree >= M:      # 자르고 남은 나무들의 길이의 합이 충분하다 -> 절단기의 높이를 올릴 수 있다
        result = mid    # result 변수에 절단기의 높이를 저장
        start = mid + 1
    else:       # 자르고 남은 나무들의 길이의 합이 충분하지 못하다 -> 나무를 더 짤라야 한다 -> 절단기의 높이를 낮추어야 한다
        end = mid - 1

print(result)


