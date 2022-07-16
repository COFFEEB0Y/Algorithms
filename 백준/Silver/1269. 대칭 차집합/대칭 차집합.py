import sys

A, B = map(int, sys.stdin.readline().split())

while True:
    set_A = set(map(int, sys.stdin.readline().split()))
    if len(set_A) == A:
        break

while True:
    set_B = set(map(int, sys.stdin.readline().split()))
    if len(set_B) == B:
        break

print(len(set_A ^ set_B))