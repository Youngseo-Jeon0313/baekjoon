import sys
input=sys.stdin.readline

N=int(input())
List=list(map(int,input().split()))
x=int(input())
left=0; right=N-1
#일단 정렬
List=sorted(List)
ans=0
while left<right :
    prefix_sum=List[left]+List[right]
    # print(prefix_sum)
    if prefix_sum<x:
        left+=1
    else:
        if prefix_sum==x: ans+=1
        right-=1
print(ans)



