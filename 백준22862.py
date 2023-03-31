import sys
input=sys.stdin.readline

S,K=map(int,input().split())
List=list(map(int,input().split()))

ans=0
left=0; right=0
limit=0
while left<=right and right<S:
    # print(left,right,limit)
    if List[right]%2==0 and limit<=K: #오른쪽 index가 짝수라면
        ans=max(ans,right-left-limit+1)
        right+=1
    else:
        if limit<K:
            right+=1
            limit+=1
        else:
            if List[left]%2: limit-=1;
            left+=1
print(ans)



    