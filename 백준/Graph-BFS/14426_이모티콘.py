# 영선이는 이미 화면에 이모티콘 1개를 입력했다. 이제, 다음과 같은 3가지 연산만 사용해서 이모티콘을 S개 만들어 보려고 한다. 

# 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
# 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
# 3. 화면에 있는 이모티콘 중 하나를 삭제한다.

# 각 연산은 1초가 걸린다.
# 영선이가 S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최솟값을 구하는 프로그램을 작성하시오.

# 이 문제에 BFS를 어떻게 적용하는지...

"""
걸리는 시간의 최솟값 -> BFS

각 연산은 1초가 걸린다 -> 에지들의 가중치가 1로 일정

노드 안의 정보 -> (s, c)    s : 화면 안의 이모티콘의 개수 , c : 클립보드 안의 이모티콘 개수

visited -> 방문처리이자 결과값(이 문제의 경우 최솟값)을 저장하는 리스트
"""

from collections import deque
import sys
input = sys.stdin.readline

# 화면에 만들 이모티콘의 개수
S = int(input())

visited = [[-1] * (S+1) for _ in range(S+1)]

queue = deque([])
queue.append([1,0])

# (1,0) 을 만드는데 0초 -> 가장 먼저 큐에 넣어주는 값
visited[1][0] = 0

while queue:
    s, c = queue.popleft()
    # 1번째 연산
    if visited[s][s] == -1: 
        visited[s][s] = visited[s][c] + 1
        queue.append([s,s])
    # 2번쨰 연산
    if s + c <= S and visited[s+c][c] == -1:
        visited[s+c][c] = visited[s][c] + 1
        queue.append([s+c, c])
    # 3번째 연산
    if s-1 >= 0 and visited[s-1][c] == -1:
        visited[s-1][c] = visited[s][c] + 1
        queue.append([s-1, c])

answer = -1
# 결과적으로 S개의 이모티콘, 즉 visited[S][] 중 최솟값을 구해야 한다
for i in range(S+1):
    if visited[S][i] != -1:
        if answer == -1 or visited[S][i] < answer:
            answer = visited[S][i]
print(answer)