ans=0

N,K=map(int,input().split())
Class=[[0 for _ in range(2)] for _ in range(6)]

#성별 학년
for _ in range(N):
    a,b=map(int,input().split())
    Class[b-1][a]+=1

# print(Class)

for i in range(6):
    for j in range(2):
        ans+=Class[i][j]//K+bool(Class[i][j]%K)

print(ans)