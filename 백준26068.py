n=int(input())
ans=0
for _ in range(n):
    day=input()
    if int(day[2::])<=90: ans+=1
print(ans)