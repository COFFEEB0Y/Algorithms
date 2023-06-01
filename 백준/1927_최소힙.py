import sys
import heapq # 파이썬의 경우 default로 min-heap

input = sys.stdin.readline

h = []

N = int(input())
for _ in range(N):
    x = int(input())
    # x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우
    if x == 0:
        if len(h) != 0:
            print(heapq.heappop(h))
        # 만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력하면 된다.
        else:
            print(0)
    # x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산
    elif x > 0:
        # max-heap 이기 때문에 앞에 -
        heapq.heappush(h, x)  

