import sys
from collections import Counter

string = sys.stdin.readline().rstrip()
string1 = string.lower()

result = []

string1 = Counter(string1).most_common()

for i in range(len(string1)):
    if string1[i][1] == (max(string1, key=lambda x: x[1]))[1]:
        result.append(string1[i][0])
if len(result) > 1:
    print('?')

else:
    s = result[0]
    print(s.upper())
