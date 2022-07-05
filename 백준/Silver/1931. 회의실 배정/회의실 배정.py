import sys
N = int(sys.stdin.readline()) # number of conference
conferences = []
ans = []
for _ in range(N):
    t = list(map(int, sys.stdin.readline().split())) # start and end time of each conference
    conferences.append(t)

conferences.sort(key= lambda x: (x[1],x[0])) # 가장 많은 수의 회의를 얻기 위해서는 회의가 끝나는 시간이 빨라야 한다.
ans.append(conferences[0]) # 정렬 기준 1. 끝나는 시간의 오름차순, 2. 시작하는 시간의 오름차순
conferences.remove(ans[0])
for conference in conferences:
    if ans[-1][1] <= conference[0]: # 이번 회의의 시작 시간이 전 회의의 종료시간보다 크거나 같으면 회의 추가
        ans.append(conference)
print(len(ans))


