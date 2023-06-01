import sys

result_stk = []     # 먼저 빠지는 순서
input_stk = []      # 이미 들어간 숫자들을 저장하는 리스트
operator_list = []

N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    result_stk.append(num)

num_list = [i for i in range(1, N+1)]  # 1~N까지의 값이 숫자 리스트에 저장됨

for num in result_stk:
    if num in input_stk:
        if num == input_stk[-1]:    # 꺼내려고 하는 값이 스택의 맨 위에 있다면 꺼낸다
            input_stk.pop()
            operator_list.append('-')
        else:
            print('NO')
            exit()

    else:                           # 스택에 들어있지 않은 값이라면
        for i in range(num_list[0],num+1):
            input_stk.append(i)     # num_list에 있는 첫 번째 값부터 num까지의 숫자들을 넣어주고
            operator_list.append('+')
            num_list.remove(i)      # 스택에 들어간 숫자들은 사용했으니 num_list에서 지워준다
        input_stk.pop()
        operator_list.append('-')
for i in operator_list:
    print(i)



