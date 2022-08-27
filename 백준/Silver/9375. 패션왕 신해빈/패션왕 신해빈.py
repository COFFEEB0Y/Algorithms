# 패션왕 신해빈

"""
 해빈이가 가진 의상들이 주어졌을때 과연 해빈이는 알몸이 아닌 상태로 며칠동안 밖에 돌아다닐 수 있을까?
 같은 종류의 의상은 하나만 입을 수 있다. 같은 이름을 가진 의상은 존재하지 않는다.
"""

import sys

# 같은 종류의 옷이 아니라면 조합할 수 있다

# 하루에 한 가지 종류의 옷만 입고 나가는 경우 + 여러 가지 종류의 옷을 입고 나가는 경우

for _ in range(int(sys.stdin.readline())):
    closet = {}
    num_of_cloth = int(sys.stdin.readline())
    for _ in range(num_of_cloth):
        cloth, cloth_type = sys.stdin.readline().split()
        if cloth_type not in closet.keys():
            closet[cloth_type] = [cloth]
        else:
            closet[cloth_type].append(cloth)
    # 여기서 종류수에 +1을 해준 이유는 그 종류의 의상을 착용해도 되고 안해도 되기 때문이고
    # 마지막에 -1을 해준 이유는 모든 의상을 착용하지 않은 경우를 제외.
    case = 1
    for i in closet.keys():
        case *= (len(closet[i])+1)
    print(case-1)








