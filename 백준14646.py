import sys
input=sys.stdin.readline

N=int(input())
Menu=list(map(int,input().split()))

state=[0 for _ in range(N+1)]
ans=0
temp=0
for i in (Menu):
    if not state[i]: state[i]=1; temp+=1
    elif state[i]==1: state[i]=-1; temp-=1
    ans=max(ans,temp)

print(ans)