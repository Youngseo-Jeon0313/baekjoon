import sys
input=sys.stdin.readline

T=int(input())
def gcd(a, b):  # 최대공약수
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)
        
for _ in range(T):
    x,y=map(int,input().split())
    print(lcm(x,y))