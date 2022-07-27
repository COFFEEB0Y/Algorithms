import sys

A, B = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())
while True:
    A_num = list(map(int, sys.stdin.readline().split()))
    if len(A_num) == m:
        break

# A진법으로 나타낸 원래의 수를 10진법으로 나타내야 함

result = [] # 출력할 B진법
num = 0 # 원래의 수

for i in range(len(A_num)):
    num += A_num[i] * (A ** ((len(A_num)-1)-i))

while num >= B:
    remainder = num % B
    num = num // B
    result.append(remainder)
result.append(num)
result = reversed(result)
print(*result)
