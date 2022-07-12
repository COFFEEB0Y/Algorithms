import sys

# 소문자 a의 아스키 코드 -> 97

result = [-1 for _ in range(26)]     # -1로 초기화 단어에 알파벳이 포함되어 있다면 갱신

word = list(sys.stdin.readline().rstrip())

for c in word:
    result[ord(c) - ord('a')] = word.index(c)   # 단어에서 해당 알파벳이 어느 index에 있는지

print(*result)


