# 일곱 난쟁이를 찾는 문제 (브루트 포스 알고리즘)
# 아홉 난쟁이의 키가 주어졌을 때, 일곱 난쟁이를 찾는 프로그램
# 일곱 난쟁이들의 키의 합은 100이며 모든 난쟁이들의 키는 다르다

import sys
from itertools import combinations

nine_dwarf = [] #아홉 난쟁이들의 키를 저장하는 리스트

for _ in range(9):
    h = int(sys.stdin.readline())
    nine_dwarf.append(h)

result = list(combinations(nine_dwarf, 7))      # 9C7 서로 다르다는 조건이 있기 때문에 조합을 사용할 수 있음

for i in range(len(result)):
    if sum(result[i]) == 100:           # 난쟁이 7곱명의 키의 합이 100이라면 그 조합을 선택
        ans = result[i]
ans = list(ans)
ans.sort()
for k in range(len(ans)):
    print(ans[k])

