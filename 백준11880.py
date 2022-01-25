import sys
input=sys.stdin.readline

t=int(input())

for i in range(t):
    L=list(map(int,input().split()))
    L.sort()
    c=L[-1]
    a=L[0]
    b=L[1]
    print(c**2+ (a+b)**2)