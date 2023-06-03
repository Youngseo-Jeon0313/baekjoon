N,T=map(int,input().split())
List=list(map(int,input().split()))
ans=0
SUM=0
for i in List:
    if SUM+i>T: break
    SUM+=i
    ans+=1
print(ans)