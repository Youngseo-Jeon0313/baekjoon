N=int(input())
List=list(map(int,input().split()))
List=sorted(List)
ans=0
for i in range(1,N):
    ans+=abs(List[i]-List[i-1])
print(ans)