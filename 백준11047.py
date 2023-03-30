N,K=map(int,input().split())
coins=[]
for _ in range(N):coins.append(int(input()))

coins.sort(reverse=True)
# print(coins)
ans=0
for i in coins: ans+=K//i; K=K%i

print(ans)