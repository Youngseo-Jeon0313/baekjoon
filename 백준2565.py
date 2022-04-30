n=int(input())
List=[0 for _ in range(100)]
dp=[0 for _ in range(100)]
for _ in range(n):
    x,y=map(int,input().split())
    List[x]=y


n=int(input())
#그냥 리스트로 만들어주는..
A=[*map(int,input().split())]
dp=[1]*n
for i in range(1,n):
    for j in range(i):
        #증가하기만 하면 그냥 일단 넣기
        if A[i]>A[j]: dp[i]=max(dp[i],dp[j]+1)
print(max(dp))