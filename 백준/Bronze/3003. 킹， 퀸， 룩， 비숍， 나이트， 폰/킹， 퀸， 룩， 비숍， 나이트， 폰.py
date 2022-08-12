import sys

King = 1
queen = 1
rook = 2
bishop = 2
knight = 2
pone = 8

K, q, r, b, k, p = map(int, sys.stdin.readline().split())

print(King-K, queen-q, rook-r, bishop-b, knight-k, pone-p)

