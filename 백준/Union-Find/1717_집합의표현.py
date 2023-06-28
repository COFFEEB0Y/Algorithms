# 유니온 파인드 : 노드가 같은 집합에 있는지 판별
# Union : 두 노드를 같은 집합으로 합치는 연산
# Find : 노드의 루트 노드를 찾는 연산

import sys
# recursionError 방지
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

# 인덱스 번호와 값이 같으면 그 노드는 루트 노드
Vroot = [i for i in range(n+1)]

def Find(x):
    if (x == Vroot[x]):
        return x
    Vroot[x] = Find(Vroot[x])
    return Vroot[x]

def Union(x, y):
    x = Find(x)
    y = Find(y)
    if x > y:
        Vroot[x] = y    
    else:
        Vroot[y] = x
    return 

def isUnion(x, y):
    if(Find(x) == Find(y)):
        print("YES")
    else:
        print("NO")
    return 

for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        Union(a, b)
    elif c == 1:
        isUnion(a, b)






