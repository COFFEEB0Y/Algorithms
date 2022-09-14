# 병합 정렬

# 반으로 나누고 정렬 -> 정렬된 배열을 다시 병합

import sys

N, K = map(int, sys.stdin.readline().split())
count = 0
ans = -1
unsorted_list = list(map(int, sys.stdin.readline().rstrip().split()))

# merge_sort함수는 재귀함수이기 때문에 임시배열을 만들게 되면 너무 메모리를 비효율적으로 사용
# merge_sort 함수
#   입력 : 정렬되지 않은 배열
#   출력 : 정렬된 배열
#   parameter : s (정렬되지 않은 배열의 첫 번째 인덱스), e(정렬되지 않은 배열의 마지막 인덱스)
def merge_sort(List, s, e):
    if s >= e: return
    mid = (s + e) // 2
    merge_sort(List, s, mid)
    merge_sort(List, mid+1, e)
    merge(List, s, mid+1, e)

# merge 함수
#   입력 : 정렬되지 않은 왼쪽 배열, 오른쪽 배열
#   출력 : 두 배열을 병합 (정렬된 배열)
#   parameter : lst(정렬하고자 하는 배열 전체), left (왼쪽 배열의 시작 인덱스), right (오른쪽 배열의 시작 인덱스), end (오른쪽 배열의 끝 인덱스)

def merge(lst, left, right, end):
    global count, ans
    tmp = []
    l, r = left, right
    while l < right and r <= end:
        if lst[l] <= lst[r]:
            tmp.append(lst[l])
            l += 1
        else:
            tmp.append(lst[r])
            r += 1
    # 둘 중 남아있는 배열을 처리
    while l < right:     # 오른쪽 배열의 숫자들이 먼저 다 쓰인 경우
        tmp.append(lst[l])
        l += 1
    while r <= end:
        tmp.append(lst[r])
        r += 1

    # 원래의 배열을 임시배열로 최신화 (정렬된 배열으로 최신화)
    l = left
    for n in tmp:
        lst[l] = n
        count += 1
        if count == K:  # 배열에 K 번째 저장되는 수
            ans = lst
            print(*ans)
            quit()
        l += 1


merge_sort(unsorted_list, 0, len(unsorted_list)-1)
print(ans)
