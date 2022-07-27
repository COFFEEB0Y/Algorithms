import sys

S = sys.stdin.readline().rstrip()

# S의 부분 문자열은 S에서 연속된 일부분을 말한다
# S의 서로 다른 부분 문자열을 출력해야 하므로 집합에 넣었다가 다시 리스트화

sub_S = [] # S의 부분 문자열들이 들어갈 리스트

for i in range(1, len(S)+1):
    for j in range(0, len(S)-i+1):
        sub_S.append(S[j:j+i])

print(len(set(sub_S)))
