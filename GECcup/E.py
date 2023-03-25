import sys
input=sys.stdin.readline

N,M=map(int,input().split())
road=list(input())
check=road.copy()
left=0;
right=0
max_left=0; max_right=0;
count=0
ans=0

while left<=right and right<N:
    # print(left, right, ans)
    if count<M:
        if check[left]=='.': #왼쪽 체크를 아직 안했다면 일단 체크
            check[left]='X'; count+=1;
            continue
        else:
            if check[right]=='.': check[right]='X'; count+=1
            right+=1;
        
    else:##이미 count가 M이니까 left 조정
        if check[right]=='X' and right-left>ans:
            ans=right-left
            max_right=right; max_left=left

        while True:
            if road[left]=='.' and check[left]=='X':
                count-=1; left+=1; break;
            else: left+=1;


print(max_left, max_right)

prefix_sum=[0 for _ in range(N)]
if road[0]=='X': 
    if max_left>0:
        prefix_sum[0]=1
    else: ans-=1


res=N
for i in range(1,N):
    if max_left<=i and i<=max_right:
            prefix_sum[i]=prefix_sum[i-1]
            continue;
    if road[i]=='X' or check[i]=='X':
        res-=1
        if road[i-1]=='X': prefix_sum[i]=prefix_sum[i-1]
        else:
            prefix_sum[i]=prefix_sum[i-1]+1
    else:
        prefix_sum[i]=prefix_sum[i-1]
what=(prefix_sum[N-1])
print(what) #몇 칸을 통째로 가는 (2) 가
print(ans) #몇 칸을 스스로 가야 하는가
print(res-ans+what*2)