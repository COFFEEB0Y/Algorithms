# 쇠막대기
import sys


class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            self.items.pop()
        except IndexError:
            print('Index Error Found')
    def __len__(self):
        return len(self.items)


parenthesis = list(sys.stdin.readline().rstrip())

stk = Stack()  # 모든 괄호가 차례로 들어가는 스택
count = 0      # 쇠막대기의 개수

for p in range(len(parenthesis)):
    if parenthesis[p] == '(':
        stk.push(parenthesis[p])

    elif parenthesis[p] == ')':
        if parenthesis[p-1] == '(':
            stk.pop()
            count += len(stk)   # 막대기의 개수 만큼을 더해준다
        else:
            stk.pop()
            count += 1

print(count)

