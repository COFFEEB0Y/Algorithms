# 최소 신장 트리 문제를 union-find를 통해 풀기
# 보통 최소 신장 트리 문제는 크루스칼 알고리즘 아니면 프림 알고리즘을 통헤 헤결 
"""
크루스칼 알고리즘I 
가중치 순으로 간선들을 오름차순으로 정렬 후 가중치가 작은 순서대로 간선들을 하나씩 삽입
만약, 그래프가 사이클을 이룬다면 그 다음으로 가중치가 작은 간선을 삽입
"""
import sys
import math
input = sys.stdin.readline


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
    return (Find(x) == Find(y))

n = int(input())
Vroot = [i for i in range(n+1)]
stars = []
edges = []

for _ in range(n):
    x, y = map(float, input().split())
    stars.append((x, y))

for i in range(n-1):
    for j in range(i+1, n):
        edges.append((i, j, math.sqrt((stars[i][0]-stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2)))

# 간선의 가중치를 기준으로 오름차순 정렬 
edges.sort(key= lambda x : x[2])

print(edges)

result = 0
for edge in edges:
    x, y, cost = edge
    if not isUnion(x, y):
        Union(x, y)
        result += cost

print(round(result, 2))







