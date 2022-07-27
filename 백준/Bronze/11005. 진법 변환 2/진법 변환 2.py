import sys

N, B = map(int, sys.stdin.readline().split())

# N을 B진법으로 바꾸는 프로그램

result = []


while N >= B:        # 남아있는 몫이 나누는 수보다 작으면 종료
    remainder = N % B
    N = N // B
    if remainder > 9:      # 나머지가 9보다 크다면
        remainder = chr(remainder + 55)
    result.append(str(remainder))

if N > 9:
    N = chr(N + 55)
result.append(str(N))
result = reversed(result)
print(''.join(result))

