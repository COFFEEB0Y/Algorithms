import sys

a, b = map(int, sys.stdin.readline().split())

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return (a*b) / gcd(a, b)

print(gcd(a,b))
print(round(lcm(a,b)))