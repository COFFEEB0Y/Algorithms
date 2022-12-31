import sys
from collections import deque

result_list = []  # 스택 수열이 따라야 하는 순서
stk_sequence = []  # 스택 수열
op_list = []

N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    result_list.append(num)

num_stk = [i for i in range(1, N+1)]
num_stk = deque(num_stk)
flag = 0

for num in result_list:
    if num in stk_sequence:
        if num == stk_sequence[-1]:  # 꺼내려고 하는 값이 스택의 맨 위에 있다면 꺼낸다
            stk_sequence.pop()
            op_list.append('-')
        else:                # 스택 수열을 만들 수 없는 경우
            print('NO')
            flag = 1
            break

    else:  # 스택에 들어있지 않은 값이라면
        while num_stk[0] <= num :  # ex) 4
            stk_sequence.append(num_stk.popleft())  # stk_sequence = [1, 2, 3, 4] / num_stk = [5, 6, 7, 8]
            op_list.append('+')
            if len(num_stk) == 0: # 덱 안에 숫자가 없다면
                break
        stk_sequence.pop()      # 4를 pop 시켜준다
        op_list.append('-')

if flag == 0:
    for i in op_list:
        print(i)
