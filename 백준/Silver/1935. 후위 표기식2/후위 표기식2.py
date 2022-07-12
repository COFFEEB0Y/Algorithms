import sys

N = int(sys.stdin.readline())
tokens = list(sys.stdin.readline().rstrip())
stk = []
operand = [] # 숫자들이 들어가는 스택
for _ in range(N):
    op = int(sys.stdin.readline())
    operand.append(op)


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 숫자들과 알파벳이 연결되어 있음

for token in tokens:
    if token in [chr(i) for i in range(ord('A'), ord('Z')+1)]:  # 토큰이 대문자 알파벳이라면 피연산자들을 스택에 넣어준다
        stk.append(operand[ord(token)-ord('A')])

    elif token in '+-/*':   # 토큰이 + 연산자라면
        try:
            a = stk.pop()       # 스택 맨 위에 있는 숫자
            b = stk.pop()       # 그 바로 아래에 있는 숫자
            if token == '+':
                stk.append(b + a)
            elif token == '-':
                stk.append(b - a)
            elif token == '/':
                stk.append(b / a)
            else:
                stk.append(b * a)
        except:
            pass
print('%0.2f' % stk[0]) # 스택의 맨 아래에 남아있는 숫자가 결국 정답이 된다