import sys
from collections import Counter

num_list = []
remove_num_list = []

N = int(sys.stdin.readline())               # 사람이 몇 명인지
increment = int(sys.stdin.readline())       # 제거되는 순서

for i in range(1,N+1):
    num_list.append(i)

idx = 0
count = 0

while (len(set(num_list))-len(set(remove_num_list))) != 1:
    if num_list[idx] not in remove_num_list:        # 제거된 숫자가 아니라면
        idx += 1    # 옆으로 한 칸
        count += 1  # 제거된 숫자가 아닌 숫자를 만나면 1씩 증가함
    else:       # 제거된 숫자라면 count는 늘리지 않지만 idx는 늘려준다
        idx += 1
    if count == increment:
        remove_num_list.append(num_list[idx-1])
        count = 0 # 다시 count를 0으로 초기화
    if idx == len(num_list):
        idx = 0  # IndexError 방지 - 다시 처음으로 돌아감

remove_num_list.append(list((set(num_list)-set(remove_num_list)))[0])
for i in range(len(remove_num_list)):
    remove_num_list[i] = str(remove_num_list[i])

print('<',", ".join(remove_num_list),'>')