import sys
input=sys.stdin.readline



N=int(input())
score=0
for i in range(N):
    a,d,g=map(int,input().split())
    if d+g==a: score=max(score,a*(d+g)*2)
    else: score=max(score,a*(d+g))

print(score)