import sys
input=sys.stdin.readline

N=int(input())
sx,sy,ex,ey=map(int,input().split())
ans=float('inf'); ans_=0
for i in range(N):
    sx_=sx;sy_=sy;ex_=ex;ey_=ey
    n=int(input())
    SUM=0
    for _ in range(n):
        x,y=map(int,input().split())
        SUM+=abs(x-sx_)+abs(y-sy_)
        sx_=x; sy_=y
    SUM+=abs(ex-sx_)+abs(ey-sy_)
    if SUM<ans: ans=SUM; ans_=i+1
print(ans_)