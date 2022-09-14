
N,K=map(int,input().split())
List=list(map(int,input().split()))
DP=[0 for _ in range(N)]
left,right=0,1
temp=0
while left<right and right<N:
    temp=sum(List[left:right+1])
    print(left,right,temp,DP)
    if temp>=K:
        if DP[right-1]<temp-K: DP[right-1]=0; DP[right]=temp-K
        if temp-List[left]<K: left+=1; right+=1; continue
        else:left=right; right+=1;
    else:right+=1
    

print(sum(DP))