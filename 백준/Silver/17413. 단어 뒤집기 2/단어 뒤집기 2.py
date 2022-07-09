import sys
from collections import deque

chs = list(sys.stdin.readline().rstrip())
ans = [] # 결과적으로 우리의 출력값
d = deque() # tag가 아닌 문자들이 들어감
tag = False # tag의 초기값을 false로 설절
# 단어가 태그라면 그대로 출력 아니라면 뒤집어서 출력

for c in chs:
    if c == ' ':
        while d:       # 태그가 아닌 값들이 들어있다면
            ans.append(d.pop())
        ans.append(c)
    elif c == '<':
        while d:
            ans.append(d.pop())
        tag = True     # start of tag
        ans.append(c)
    elif tag and c == '>':                  # 먼저 와야 하는 조건!!!
        tag = False  # end of tag
        ans.append(c)
    elif tag:          # 태그라면 바로 ans리스트에 넣어줌
        ans.append(c)
    elif not tag:      # 태그가 아니라면 d에 넣어준다
        d.append(c)
while d: # 스택에 태그가 아닌 값들이 남아있다면
    ans.append(d.pop())

print(''.join(ans))






