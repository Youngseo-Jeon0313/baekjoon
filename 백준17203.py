import sys
input=sys.stdin.readline

N,Q=map(int,input().split())
Rhythm=list(map(int,input().split()))
List=[0 for _ in range(N)]
for i in range(1,N):
    List[i]=abs(Rhythm[i]-Rhythm[i-1])
prefixsum=[0 for _ in range(N)]
for i in range(1,N):
    prefixsum[i]=prefixsum[i-1]+List[i]
for _ in range(Q):
    x,y=map(int,input().split())
    print(prefixsum[y-1]-prefixsum[x-1])