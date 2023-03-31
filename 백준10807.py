N=int(input())
List=list(map(int,input().split()))
find=int(input())
ans=0
for i in List: 
    if i==find: ans+=1

print(ans)