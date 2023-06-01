import sys

# 단어장에 들어있는 단어들 <단어 + 단어가 나온 횟수>
words = dict()

N, M = map(int, sys.stdin.readline().split())

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) < M:
        continue
    else:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

# 단어장의 앞부분에 배치할지 뒤에 배치할지 결정하는 요소
# 1. 자주 나오는 단어일수록 앞에 배치한다.
# 2. 해당 단어의 길이가 길수록 앞에 배치한다.
# 3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다

"""
# sorted는 다중기준을 설정할 수 있다
파이썬의 sort 및 sorted 함수는 key 인자 값으로 정렬에 있어서 우선 순위 기준을 설정 할 수 있다.
sort(key= lambda x: (기준1, 기준2, 기준3))
해당 문제에서는 개수, 길이는 내림차순으로 단어순서는 오름차순으로 설정하라고 했으므로 개수와 길이 기준 앞에 마이너스(-)를 붙였다
"""

word_note = sorted(words.items(), key= lambda x : (-x[1], -len(x[0]), x[0]))
for word in word_note:
    print(word[0])