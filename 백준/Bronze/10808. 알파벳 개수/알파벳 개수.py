import sys

# 소문자 a의 아스키 코드 -> 97

result = [0 for _ in range(26)]     # 알파벳 소문자의 개수가 26개

word = list(sys.stdin.readline().rstrip())

for c in word:
    result[ord(c) - ord('a')] += 1

print(*result)



