import sys
input=sys.stdin.readline

from itertools import permutations as cb
N,M=map(int,input().split())
List=[i for i in range(N)]
L=list(map(int,input().split()))
Ans=0
for k in L:
    if k==M: Ans+=1
for i in list(cb(List,2)):
    sum=0
    for j in range(i[0],i[1]+1):
        sum+=L[j]
    if sum==M: Ans+=1
print(Ans)