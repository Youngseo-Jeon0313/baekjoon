import sys
input=sys.stdin.readline

N=int(input())
s=input()
ans=0
LR=[0 for _ in range(N)]
SK=[0 for _ in range(N)]
flag=True
for i in range(N):
    if 49<=ord(s[i]) and ord(s[i])<=57:
        ans+=1
        if i!=0:
            LR[i]=LR[i-1]
            SK[i]=SK[i-1]
    if s[i]=='L':
        LR[i]=LR[i-1]+1
        SK[i]=SK[i-1]
    if s[i]=='R':
        if LR[i-1]>0:
            LR[i]=LR[i-1]-1
            SK[i]=SK[i-1]
            ans+=1
        else: break;
    if s[i]=='S':
        SK[i]=SK[i-1]+1
        LR[i]=LR[i-1]
    if s[i]=='K':
        if SK[i-1]>0:
            SK[i]=SK[i-1]-1
            LR[i]=LR[i-1]
            ans+=1
        else: break;
print(ans)
