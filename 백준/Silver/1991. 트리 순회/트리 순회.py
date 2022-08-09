# 트리 자료 구조 구현

import sys


class Node:
    def __init__(self, root, left_node, right_node):
        self.root = root
        self.left_node = left_node
        self.right_node = right_node


# 전위 순회 - (루트)(왼쪽자식)(오른쪽자식)
def pre_order_traversal(node):  # 인자의 값으로 Node타입의 객체가 들어와야 한다
    print(node.root, end='')  # 일단 루트 노드 먼저 출력
    if node.left_node != '.':
        pre_order_traversal(tree[node.left_node])
    if node.right_node != '.':
        pre_order_traversal(tree[node.right_node])


# 중위 순회 - (왼쪽자식)(루트)(오른쪽자식)
def in_order_traversal(node):
    if node.left_node != '.':
        in_order_traversal(tree[node.left_node])
    print(node.root, end='')
    if node.right_node != '.':
        in_order_traversal(tree[node.right_node])


# 후위 순회 - (왼쪽자식)(오른쪽자식)(루트)
def post_order_traversal(node):
    if node.left_node != '.':
        post_order_traversal(tree[node.left_node])
    if node.right_node != '.':
        post_order_traversal(tree[node.right_node])
    print(node.root, end='')


N = int(sys.stdin.readline())  # 이진 트리의 노드의 개수
tree = {}  # 각 노드들을 딕셔너리 형태로 트리 자료구조에 저장

for _ in range(N):
    root, left_node, right_node = sys.stdin.readline().rstrip().split()
    tree[root] = Node(root, left_node, right_node)  # 노드 클래스로 만들어진 노드 타입의 객체를 값으로 받음

pre_order_traversal(tree['A'])
print()  # 줄바꿈
in_order_traversal(tree['A'])
print()
post_order_traversal(tree['A'])
