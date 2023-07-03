ans=0
N=int(input())
for i in range(1,N+1):
    List=list(str(i))
    sum=0
    for j in List:
        sum+=int(j)
    if i%sum==0: ans+=1

print(ans)