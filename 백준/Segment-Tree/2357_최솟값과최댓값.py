
# 그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 합을 구하려 한다
# 세그먼트 트리 활용!
import sys
input = sys.stdin.readline

# merge함수를 바꾸면 구간합이 아닌 최댓값, 최솟값 등을 담고 있는 형태로 변경이 가능하다
# 두 개의 노드를 합치는 경우 
def merge(left1, left2, right1, right2):
    _min = min(left1, left2)
    _max = max(right1, right2)
    return _min, _max

def build(stree, node, left, right):
    if left == right:
        stree[node][0] = num_list[left]
        stree[node][1] = num_list[left]
        return stree[node][0], stree[node][1]
    mid = left + (right-left) // 2
    min_left_val, max_left_val = build(stree, 2*node, left, mid)
    min_right_val, max_right_val = build(stree, 2*node+1, mid+1, right)
    stree[node][0], stree[node][1] = merge(min_left_val,min_right_val,max_left_val,max_right_val)    
    return stree[node][0], stree[node][1]

def query(start, end, node, left, right):
    if end < left or start > right:
        # 일부로 최대, 최소값을 넣어준다. -> 다음 시행에 영향을 주지 않기 위해서 
        return 1000000000, 1
    
    if start <= left and right <= end:
        return stree[node][0], stree[node][1]
    
    mid = left + (right-left) // 2
    min_left_val, max_left_val = query(start, end, 2*node, left, mid)
    min_right_val, max_right_val =  query(start, end, 2*node+1, mid+1, right)
    stree[node][0], stree[node][1] = merge(min_left_val,min_right_val,max_left_val,max_right_val)    
    return stree[node][0], stree[node][1]

# def update(idx, val, node, left, right):
#     if idx < left or idx > right:
#         return stree[node]
    
#     if left == right:
#         stree[node] = val
#         return stree[node]
    
#     mid = left + (right-left) // 2
#     left_val = update(idx, val, 2*node, left, mid)
#     right_val = update(idx, val, 2*node+1, mid+1, right)
#     stree[node] = merge(left_val, right_val)
#     return stree[node]



N, M= map(int, input().split())
# 배열 생성
num_list = []
for _ in range(N):
    num_list.append(int(input()))
# 세그먼트 트리 생성 -> 노드 안에 최솟값과 최댓값 모두를 담아야 한다 
stree = [[0, 0] for x in range(4*len(num_list))]

build(stree, 1, 0, len(num_list)-1)

for _ in range(M):
    # a=1, b=3이라면 입력된 순서대로 1번, 2번, 3번 정수 중에서 최소, 최댓값
    a, b= map(int, input().split())
    _min, _max = query(a-1, b-1, 1, 0, len(num_list)-1) 
    print(_min, _max)
