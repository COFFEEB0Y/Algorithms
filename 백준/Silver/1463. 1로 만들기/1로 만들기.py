import sys

N = int(sys.stdin.readline())
"""
동적 프로그래밍은 큰 문제를 작은 문제로 나누는 것
문제들을 매번 재계산하지 않고 값을 저장해두었다가 재사용하는 기법 (Memoization)
"""
d = [0 for _ in range(N+1)]         # d[n] -> n을 1로 만드는데 필요한 연산의 횟수
                                    # d[0], d[1]의 값은 1
for i in range(2, N+1):             # d(N) = min(d(N-1)+1, d(N//3)+1, d(N//2)+1)
    d[i] = d[i-1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)   # 6의 배수는 두 가지의 조건식을 모두 지나야 함 -> 따라서 둘 다 if문으로
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
print(d[N])