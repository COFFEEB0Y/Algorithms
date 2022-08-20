import sys

N = int(sys.stdin.readline())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 한 변의 길이가 N인 종이

# 하얀색으로 칠해진 칸은 0, 파란색으로 칠해진 칸은 1로 주어진다

result = []

def solution(x, y, N) :
  color = paper[x][y]   # 모두 같은 색으로 칠해져 있는지 판별 <가장 처음 정사각형의 색을 저장하고 나머지 정사각형들과 비교>
  for i in range(x, x+N):
    for j in range(y, y+N):
      if color != paper[i][j]: # 모두 같은 색으로 칠해져 있지 않으면 같은 방법으로 똑같은 크기의 네 개의 색종이로 나눈다. -> 재귀 조건
        solution(x, y, N//2)        # 나누어진 색종이도 똑같이 진행
        solution(x, y+N//2, N//2)
        solution(x+N//2, y, N//2)
        solution(x+N//2, y+N//2, N//2)
        return
  if color == 0 :
    result.append(0) # 모두 같은 색으로 칠해져 있는 종이의 색이 하얀색
  else :
    result.append(1) # 모두 같은 색으로 칠해져 있는 종이의 색이 파란색


solution(0,0,N)
print(result.count(0)) # 흰색 종이의 개수
print(result.count(1)) # 파란색 종이의 개수

