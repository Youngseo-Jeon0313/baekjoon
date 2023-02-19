N=int(input())
L=list(int(input()) for _ in range(N))
L.sort()
ans=0
for i in range(N):
    ans+=abs(L[i]-(i+1))

print(ans)