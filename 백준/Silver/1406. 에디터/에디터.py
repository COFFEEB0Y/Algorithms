import sys

stk_l = list(sys.stdin.readline().rstrip())
stk_r = []
for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == 'L':
        if stk_l:       # 커서를 기준으로 왼쪽 스택이 비어있지 않다면
            stk_r.append(stk_l.pop())
    elif command[0] == 'D':
        if stk_r:
            stk_l.append(stk_r.pop())
    elif command[0] == 'B':
        if stk_l:
            stk_l.pop()     # 커서 왼쪽에 있는 문자를 삭제
    elif command[0] == 'P':
        stk_l.append(command[1])

stk_l.extend(reversed(stk_r))
print(''.join(stk_l))


