# 백트래킹으로 풀기

# 순열을 중복없이 출력하는 문제 -> 중복인지 아닌지 check!

import sys

N, M = map(int, sys.stdin.readline().split())
Ns = list(map(int, sys.stdin.readline().split()))
Ns.sort()


s = []

visited = [False] * len(Ns)     # visited로 숫자를 구별한다


def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    overlap = 0
    for i in range(len(Ns)):
        if not visited[i] and overlap != Ns[i]:      # 같은 수를 처리할 수 있음
            s.append(Ns[i])
            visited[i] = True
            overlap = Ns[i]
            dfs()
            visited[i] = False  # 함수가 빠져나오면서 방문처리 해제
            s.pop()


dfs()

