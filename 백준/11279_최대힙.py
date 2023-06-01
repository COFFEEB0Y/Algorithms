"""
힙(Heap)
- 완전 이진 트리 자료구조의 일부
- 힙에서 항상 루트 노드를 제거
-> 최소 힙 : 루트 노드가 가장 작은 값을 가짐 => 출력 시 오름차순
-> 최대 힙 : 루트 노드가 가장 큰 값을 가짐 => 출력 시 내림차순

데이터의 개수가 N개일 때, 삽입시간과 삭제시간이 모두 O(NlogN)으로 동일하다.
"""
import sys
import heapq # 파이썬의 경우 default로 min-heap

input = sys.stdin.readline

# 힙 정렬(min-heap) -> 이터러블 객체를 넣으면 오름차순으로 출력 
# def heapsort(iterable):
#     h = []
#     result = []
#     for value in iterable:
#         heapq.heappush(h, value)    // max-heap으로 바꾸고 싶으면 heapq.heappush(h, -value)
#     for i in range(len(h)):
#         result.append(heapq.heappop(h)) // max-heap으로 바꾸고 싶으면 result.append(-heapq.heappop(h))
#     return result

# lst = [1, 5, 2, 7, 3]
# res = heapsort(lst)
# print(*res)



h = []

N = int(input())
for _ in range(N):
    x = int(input())
    # x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우
    if x == 0:
        if len(h) != 0:
            print(-heapq.heappop(h))
        # 만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력하면 된다.
        else:
            print(0)
    # x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산
    elif x > 0:
        # max-heap 이기 때문에 앞에 -
        heapq.heappush(h, -x)  




