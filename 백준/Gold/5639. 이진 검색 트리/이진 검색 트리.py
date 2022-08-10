# 이진검색트리

"""
이진 검색 트리를 전위 순회한 결과가 주어졌을 때, 이 트리를 후위 순회한 결과를 구하는 프로그램을 작성하시오.
(루트)(왼쪽자식)(오른쪽자식)
"""

import sys
sys.setrecursionlimit(10**7)


def dfs(start, end):

    # 시작과 끝 값이 역전시 리턴
    if start > end:
        return

    temp = end + 1

    # 서브 트리 찾기
    for i in range(start + 1, end + 1):
        # 루트 보다 크면 오른쪽 서브 트리
        if graph[start] < graph[i]:
            temp = i
            break

    dfs(start + 1, temp - 1) # 왼쪽 서브 트리 재귀적으로 탐색
    dfs(temp, end) # 오른쪽 서브 트리 재귀적으로 탐색

    print(graph[start])


graph = []
while True:
    try:
        num = int(sys.stdin.readline())
        graph.append(num)
    except:     # 아무 에러가 발생하면 반복문 종료
        break

dfs(0, len(graph)-1)
