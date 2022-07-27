N,K=map(int,input().split())

List=list(map(int,input().split()))
maxNum=max(List)
#print(maxNum)
count=[0 for _ in range(maxNum+1)]
left=0; right=0;

ans=0
while right<N:
    if count[List[right]]<K:
        count[List[right]]+=1;
        right+=1
        # if right==N-1: 
        #     if count[List[right]]>K:
        #         left+=1;
        #     break;
    else:
        count[List[left]]-=1;
        left+=1
    #print(left,right)
    ans=max(ans,right-left)
print(ans)