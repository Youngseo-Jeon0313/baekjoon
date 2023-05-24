T=int(input())
L=list(map(int,input().split()))
ans=0
for i in L:
    if i==T: ans+=1

print(ans)