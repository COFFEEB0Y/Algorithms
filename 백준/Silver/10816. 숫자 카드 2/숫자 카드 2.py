from sys import stdin
_ = stdin.readline()
N = map(int,stdin.readline().split())
_ = stdin.readline()
M = map(int,stdin.readline().split())
hashmap = {}
for n in N:
    if n in hashmap:
        hashmap[n] += 1
    else:
        hashmap[n] = 1
ans = []
for m in M:
    if m in hashmap.keys():
        ans.append(hashmap[m])
    else:
        ans.append(0)
for i in ans:
    print(i, end=" ")

