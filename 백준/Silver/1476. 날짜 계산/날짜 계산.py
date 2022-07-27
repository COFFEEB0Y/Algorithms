"""
날짜 계산 문제
준규 나라에서의 연도 -> 우리가 아는 연도
"""

import sys

E, S, M = map(int, sys.stdin.readline().split())    # 지구 E, 태양 S, 달 M

E_lst = []
S_lst = []
M_lst = []

E_lst.append(E)
S_lst.append(S)
M_lst.append(M)


while len(set(E_lst) & set(S_lst) & set(M_lst)) == 0:
    E += 15
    S += 28
    M += 19
    E_lst.append(E)
    S_lst.append(S)
    M_lst.append(M)

print(list((set(E_lst) & set(S_lst) & set(M_lst)))[0])
