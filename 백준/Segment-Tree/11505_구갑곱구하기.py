
# 그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 합을 구하려 한다
# 세그먼트 트리 활용!
import sys
input = sys.stdin.readline

# merge함수를 바꾸면 구간합이 아닌 최댓값, 최솟값 등을 담고 있는 형태로 변경이 가능하다
def merge(left, right):
    # 곱셈의 경우 숫자가 매우 커질 수 있기 때문에 중간에 숫자를 줄여주는 작업이 필요(보통 문제에 제시되어 있음)
    return (left*right) % 1000000007

def build(stree, node, left, right):
    if left == right:
        stree[node] = num_list[left]
        return stree[node]
    mid = left + (right-left) // 2
    left_val = build(stree, 2*node, left, mid)
    right_val = build(stree, 2*node+1, mid+1, right)
    stree[node] = merge(left_val, right_val)    
    return stree[node]

def query(start, end, node, left, right):
    # 구간의 곱셈을 구할 떄는 구간합을 구할 때와 다르게 관심구역(start~end)를 완전히 벗어나더라도 return 값을 1로 
    if end < left or start > right:
        return 1
    
    if start <= left and right <= end:
        return stree[node]
    
    mid = left + (right-left) // 2
    left_val = query(start, end, 2*node, left, mid)
    right_val =  query(start, end, 2*node+1, mid+1, right)
    return merge(left_val, right_val)

def update(idx, val, node, left, right):
    if idx < left or idx > right:
        return stree[node]
    
    if left == right:
        stree[node] = val
        return stree[node]
    
    mid = left + (right-left) // 2
    left_val = update(idx, val, 2*node, left, mid)
    right_val = update(idx, val, 2*node+1, mid+1, right)
    stree[node] = merge(left_val, right_val)
    return stree[node]



N, M, K = map(int, input().split())
# 배열 생성
num_list = []
for _ in range(N):
    num_list.append(int(input()))
# 세그먼트 트리 생성
stree = [0 for x in range(4*len(num_list))]

build(stree, 1, 0, len(num_list)-1)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b-1, c, 1, 0, len(num_list)-1)
    elif a == 2:
        res = query(b-1, c-1, 1, 0, len(num_list)-1) 
        print(res)
