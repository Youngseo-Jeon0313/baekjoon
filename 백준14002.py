n=int(input())
#그냥 리스트로 만들어주는..
A=list(map(int,input().split()))
#LIS 로직
dp=[1]*n
for i in range(1,n):
    for j in range(i):
        #증가하기만 하면 그냥 일단 넣기
        if A[i]>A[j]: dp[i]=max(dp[i],dp[j]+1)


ans=[]

std=max(dp)
print(std)

for i in range(n-1,-1,-1):
        if dp[i]==std:
            ans.append(A[i])
            std-=1

for i in ans[::-1]:
    print(i,end=' ')

