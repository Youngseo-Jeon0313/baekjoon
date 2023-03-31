N,K=map(int,input().split())
ans=1
for i in range(N,N-K,-1):
    ans*=i
# print(ans)
for j in range(1,K+1):
    ans//=j
print(ans)