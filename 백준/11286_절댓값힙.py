"""
단, 절댓값을 기준으로 정렬해야하지만 출력되는 값은 기존 값이여야 한다.
튜플을 비교할 때 첫 번째 원소를 기준으로 정렬하기 때문에 (절댓값, 기존 값) 튜플 형식으로 힙에 넣는다.
heap을 tuple로 구성했을 때 맨 앞 숫자만 가지고 정렬한다
"""
import sys
import heapq 

input = sys.stdin.readline

h = []

N = int(input())
for _ in range(N):
    x = int(input())
    # x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우
    if x == 0:
        if len(h) != 0:
            print(heapq.heappop(h)[1])
        # 만약 배열이 비어 있는 경우인데 절댓값이 가장 작은 값을 출력하라고 한 경우에는 0을 출력
        else:
            print(0)
    # x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산
    elif x != 0:
        heapq.heappush(h, (abs(x), x))  
