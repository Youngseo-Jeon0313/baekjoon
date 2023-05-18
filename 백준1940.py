import sys
input=sys.stdin.readline

N=int(input())
M=int(input())
List=list(map(int,input().split()))
List=sorted(List)
ans=0
# 1 2 3 4 5 7
left=0; right=N-1
while left<right:
    SUM=List[left]+List[right]
    if SUM<M: left+=1
    else :
        if SUM==M: ans+=1
        right-=1
    # print(ans,left,right)


print(ans)