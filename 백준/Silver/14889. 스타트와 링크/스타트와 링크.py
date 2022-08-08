# 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력


import sys
from itertools import combinations, permutations

N = int(sys.stdin.readline())

ability = []
for _ in range(N):
    ability.append(list(map(int, sys.stdin.readline().split())))

member = N // 2 # 한 개의 팀 안에 속하는 사람 수

# N명의 사람들로 만들어질 수 있는 팀의 가지수
cases = list(combinations(range(1,N+1), member))

# cases에서 대칭되는 요소들의 차이가 최소인 값을 찾으면 된다

team_abilities = [] # 팀들의 능력치가 모여있는 리스트
# 팀의 능력치 구하기
for i in cases:
    team_ability = 0
    case = list(permutations(i, 2))
    for j in case:
        a, b = j
        team_ability += ability[a-1][b-1]
    team_abilities.append(team_ability)


# 팀들간의 능력치 차이
team_ability_difference = []
for i in range((len(team_abilities) // 2)):
    team_ability_difference.append(abs(team_abilities[i] - team_abilities[-(i+1)]))

print(min(team_ability_difference)) # 팀들간의 능력치 차이 중 최소값울 출력


