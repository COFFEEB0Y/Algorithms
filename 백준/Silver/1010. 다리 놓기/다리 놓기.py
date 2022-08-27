# 다리놓기
"""다리끼리는 서로 겹쳐질 수 없다고 할 때 다리를 지을 수 있는 경우의 수를 구하는 프로그램을 작성하라."""
# 왼쪽에 사이트가 4개 있다면 , 오른쪽 사이트에서 4개의 사이트를 고르기만 하면 된다

import sys
import math


# 조합을 구하는 공식

for _ in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    bridges = math.factorial(M) // (math.factorial(N) * math.factorial(M-N))
    print(bridges)

