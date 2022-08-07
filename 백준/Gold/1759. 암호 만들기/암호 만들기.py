# # 암호 (백준 #1759)
# # 서로 다른 C개의 알파벳으로 L자리수 암호를 만드는 조합 문제 (원소들 간에 서열 있다)
import sys
L, C = map(int, sys.stdin.readline().split()) # L자리수 암호
lst = sorted(list(map(str, sys.stdin.readline().split())))  # 사용할 수 있는 알파벳들이 들어있는 리스트
visited = [False] * C
vowels = ['a', 'e', 'u', 'i', 'o']
s = []

def dfs(L, C):
    if len(s) == L:
        sub_set = [x for x in s if x not in vowels]
        # 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성
        for vowel in vowels:
            if vowel in s and len(sub_set) >= 2:
                print(''.join(s))
                break
        return

    if len(s) == 0: # 스택이 비어있다면
        z = -1    # 스택 내 가장 우측 원소의 인덱스를 0으로 설정
    else:
        z = lst.index(s[-1])

    for i in range(C):
        if not visited[i] and i > z:    # 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열
            s.append(lst[i])            # abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.
            visited[i] = True
            dfs(L, C)
            visited[i] = False
            s.pop()


dfs(L, C)

