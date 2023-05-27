n=int(input())
ans=0
for i in range(1,n+1):
    for j in str(i):
        if j in ['3','6','9'] : ans+=1

print(ans)