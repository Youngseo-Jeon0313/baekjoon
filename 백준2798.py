from itertools import combinations as cb
N,M=map(int,input().split())
List=list(map(int,input().split()))
ans=0
for i in cb(List,3):
    if sum(i) <=M : ans=max(ans,sum(i))
print(ans)    