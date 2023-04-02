N=int(input())
List=list(map(int,input().split()))

ans=0
SUM=sum(List)
#꿀이 벌들 사이에 있을 때는 무조건 벌이 양 끝에 있는 게 이득이다!
temp=(SUM-List[0]-List[-1])
for i in range(1,N-1):
    ans=max(ans,temp+List[i])

#꿀이 왼쪽 끝에 있을 때는, 벌 하나는 오른쪽 끝에 있는 게 이득이다.
temp=SUM-List[-1] #오른쪽 끝의 벌 삭제
prefix_sum=0
for i in range(N-2,0,-1):
    ans=max(ans,prefix_sum+2*(temp-prefix_sum-List[i]))
    prefix_sum+=List[i]

#꿀이 오른쪽 끝에 있을 때는 벌 하나는 왼쪽 끝에 있는 게 이득이다.
temp=SUM-List[0] #왼쪽 끝의 벌 삭제
prefix_sum=0
for i in range(1,N-1):
    ans=max(ans,prefix_sum+2*(temp-prefix_sum-List[i]))
    prefix_sum+=List[i]
print(ans)