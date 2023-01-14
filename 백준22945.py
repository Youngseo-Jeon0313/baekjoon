import sys
input=sys.stdin.readline


#right가 left보다 작다면 무조건 right을 왼쪽으로 움직이는 게 이득
N=int(input())

List=list(map(int,input().split()))

ans = 0
left=0; right=N-1

while left+1 <= right:
    ans=max(ans,min(List[left], List[right])*(right-left-1))
    if List[right]<List[left]:
        right-=1
    else:
        left+=1
print(ans) 