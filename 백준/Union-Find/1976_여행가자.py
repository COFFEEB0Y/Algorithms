# 같은 도시를 여러 번 방문하는 것도 상관이 없다
# 동혁이의 여행 계획에 속한 도시들이 순서대로 주어졌을 때 여행경로를 통해 달성이 가능한지는 모든 도시들이 연결되어 있는지를 물어보는 것
# 노드들이 서로 연결되어 있는지(같은 집합에 있는지)를 물어보는 문제는 유니온 파인트들 통해 해결할 수 있다
# 루트 노들의 값을 비교해 같은 집합에 속하는지 알 수 있다


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
M = int(input())

Vroot = [i for i in range(N+1)]

def find(x):
    if (x == Vroot[x]):
        return x
    Vroot[x] = find(Vroot[x])
    return Vroot[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        Vroot[x] = y
    else:
        Vroot[y] = x
    return

def isUnion(*args):
    f = find(args[0])
    for arg in args:
        if(f != find(arg)):
            print("NO")
            return
    print("YES")


for i in range(N):
    cities = list(map(int, input().split()))
    for j in range(len(cities)):
        if cities[j] == 1:
            union(i+1, j+1)
        else:
            pass

vacation_plan = list(map(int, input().split()))
isUnion(*vacation_plan)