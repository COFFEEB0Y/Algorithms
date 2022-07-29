# 이분 탐색을 이용한 수 찾기
import sys

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

N = int(sys.stdin.readline()) # 수열 A안에 있는 수들의 개수
while True:
    A = list(map(int, sys.stdin.readline().split()))
    if len(A) == N:
        break
A.sort()

M = int(sys.stdin.readline()) # 수열 B안에 있는 수들의 개수
while True:
    B = list(map(int, sys.stdin.readline().split()))  # 이 수들이 A안에 존재하는지 알아내면 된다
    if len(B) == M:
        break

for i in B:
    print(binary_search(A, i, 0, len(A)-1))

