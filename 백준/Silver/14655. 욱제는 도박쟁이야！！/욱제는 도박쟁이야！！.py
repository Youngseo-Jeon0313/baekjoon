n=int(input())

mx=list(map(int,input().split()))
mn=list(map(int,input().split()))
sm,sn=0,0
for i in mx:
    sm+=abs(i)
for i in mn:
    sn+=abs(i)
print(sm+sn)