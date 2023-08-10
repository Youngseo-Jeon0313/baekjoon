def count_one(x):
    ans=0
    x=bin(x)
    for i in x:
        if i=='1': ans+=1
    return ans
N=int(input())
List=list(map(int,input().split()))

if N==1: print(0)
else:
    DP=[0 for _ in range(N)]
    DP[1]=count_one(List[0]^List[1])
    
    for i in range(2,N):
        DP[N-2]=0
        if i>=1 and i!=2:
            DP[i]=max(DP[i],DP[i-2]+count_one(List[i-1]^List[i]))
        if i>=2 and i!=3:
            DP[i]=max(DP[i],DP[i-3]+count_one(List[i-2]^List[i-1]^List[i]))
        if i==N-2: DP[i]=0
    print(DP[-1])
# print(DP)