import sys
input=sys.stdin.readline

N,M=map(int,input().split())
List=[0 for _ in range(1,N+2)]


start=1
end=N


flag=True
for k in range(1,N+1):
    if M>=N-k:M-=(N-k); List[k]=end; end-=1
    else: List[k]=start; start+=1

if start<=end or M!=0: print(-1)
else: print(*List[1:])