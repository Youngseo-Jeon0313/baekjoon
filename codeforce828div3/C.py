import sys
input=sys.stdin.readline
from collections import deque

t=int(input())
for _ in range(t):
    ans=0
    n,type=input().split()
    n=int(n)
    S=str(input())
    TYPE=[]
    GREEN=[]
    flag=False
    for i in range(n):
        if S[i]=='g' and not flag: GREEN.append(i); GREEN.append(i+n); flag=True
        if S[i]==type: TYPE.append(i)
    GREEN.sort()
    GREEN=deque(GREEN)
    for k in TYPE:
        if len(GREEN):
            while len(GREEN) and GREEN[0]<k:
                a=GREEN.popleft()
            ans=max(ans,GREEN.popleft()-k)
    print(ans)

