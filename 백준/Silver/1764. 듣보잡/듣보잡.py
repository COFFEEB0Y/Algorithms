import sys

N, M = map(int, sys.stdin.readline().split())
h = []
l = []
for _ in range(N):
    s = sys.stdin.readline().rstrip()
    h.append(s)
for _ in range(M):
    s = sys.stdin.readline().rstrip()
    l.append(s)

ans_list = list(set(h) & set(l))
ans_list.sort()
print(len(ans_list))
for i in ans_list:
    print(i)