import sys

S = sys.stdin.readline().rstrip()
ans = []

for i in range(len(S)):
    ans.append(S[i:])

ans.sort()
for j in range(len(ans)):
    print(ans[j])