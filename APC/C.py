import sys
input=sys.stdin.readline

N=int(input())
List=list(map(int,input().split()))
ans=0
for i in range(N-1):
    if List[i]>=List[i+1]: ans+=1
if List[0]>List[-1]: ans-=1
print(ans+1)