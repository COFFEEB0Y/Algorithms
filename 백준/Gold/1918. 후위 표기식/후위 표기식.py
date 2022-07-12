import sys

tokens = list(sys.stdin.readline().rstrip())
stk = []  # operator들이 들어가는 스택
result = []  # 우리가 출력할 리스트

for token in tokens:
    if token in [chr(i) for i in range(ord('A'), ord('Z') + 1)]:  # 토근이 대문자 알파벳이라면
        result.append(token)
    else:  # 토큰이 연산자라면
        if token == '(':  # 왼쪽 괄호가 들어온다면 무조건 스택에 push
            stk.append(token)
        elif token == ')':
            while stk and stk[-1] != '(': # 오른쪽 괄호가 들어온다면 왼쪽 괄호가 나올 때까지 스택 안에 있는 모든 연산자들을 pop하고 '('마저 뺴준다
                result.append(stk.pop())
            stk.pop()   # ( 를 스택에서 빼준다
        elif token == '-' or token == '+':    # +, - 는 ( 보다는 우선순위가 높지만 대체로 낮은 편 -> 웬만하면 스택 안의 값들을 pop함
            while stk and stk[-1] != '(': # 스택이 비어있거나 스택 맨위의 값이 ( 이면 멈춤
                result.append(stk.pop())
            stk.append(token) # 자기 자신은 스택에 들어가야 함
        else:
            while stk and stk[-1] != '(' and (stk[-1] == '*' or stk[-1] == '/'):   # 동일한 우선순위에 있는 연산자들 또한 모두 pop
                result.append(stk.pop())
            stk.append(token)   # *, / 와 같은 연산자들은 그냥 stk에 올라감

if len(stk) != 0:   # 스택에 남아있는 연산자가 있다면 나머지를 result리스트에 추가해준다
    for _ in range(len(stk)):
        result.append(stk.pop())

if ('(' or ')') in result:
    result.remove('(')
    result.remove(')')

print("".join(result))
