import sys
input = sys.stdin.readline

def GCD_two_number(a, b):
    while b!=0:
        a, b = b, a%b
    return a

def GCD_several_numbers(arr):
    gcdarr = arr[0]
    for i in range(len(arr)):
        gcdarr = GCD_two_number(gcdarr, arr[i])
    return gcdarr

# 가로수가 있는 위치
tree_pos = []
# 가로수가 있는 위치들의 사이값
split_distances = []

for _ in range(int(input())):
    tree_pos.append(int(input()))

for i in range(len(tree_pos)-1):
    split_distances.append(tree_pos[i+1]-tree_pos[i])


# 사잇값들의 최대공약수 찾기 -> 가로수가 띄워져 있는 거리
split_distance = GCD_several_numbers(split_distances)

# 간격을 최대공약수로 나누고 1을 빼주면 사이에 심을 나무 숫자가 나온다
add_num = 0
for i in split_distances:
    add_num += i // split_distance - 1

print(add_num)


