import sys

N, B = sys.stdin.readline().split()
# B진법 수 N을 10진법으로 바꾸는 프로그램

lst = []
for i in N:
    lst.append(i)

result = 0

for i in range(len(lst)):     # 0~4
    if lst[i].isalpha():
        lst[i] = ord(lst[i])-55
        result += lst[i] * (int(B) ** ((len(lst)-1)-i))
        continue
    result += int(lst[i]) * (int(B) ** ((len(lst)-1)-i))
print(result)

