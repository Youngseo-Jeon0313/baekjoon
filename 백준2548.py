N=int(input())
List=list(map(int,input().split()))
ans=float('inf'); sum=float('inf')
for i in range(N):
    temp_sum=0
    for j in range(N):
        temp_sum+=abs(List[i]-List[j])
    if temp_sum<=sum: 
        if temp_sum==sum:
            ans=min(ans,List[i]); 
        else: ans=List[i]
        sum=temp_sum
    # print(temp_sum,sum,ans)
print(ans)