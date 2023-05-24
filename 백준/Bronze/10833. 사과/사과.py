
ans=0
n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    ans+=b%a
print(ans)