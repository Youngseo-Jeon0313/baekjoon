import sys
input=sys.stdin.readline

N,K=map(int,input().split())
List=list(map(int,input().split()))
DP=[0 for _ in range(N)]
left,right=0,1
temp=List[left]
flag=False
ans=0
temp_ans=0
while left<right and right<N:
    #print(left,right,temp,DP)
    temp+=List[right]
    if flag==True: temp=List[left]+List[right]; flag=False
    if temp>=K:
        if DP[right-1]<=temp-K: temp_ans-=DP[right-1];temp_ans+=temp-K; DP[right-1]=0; DP[right]=temp-K; 
        if temp-List[left]<=K: temp-=List[left];left+=1; right+=1; 
        else:left=right; flag=True; right+=1;
    else:right+=1
    ans=max(ans, temp_ans)
# print(DP)
print(ans)