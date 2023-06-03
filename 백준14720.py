turn=0
n=int(input())
List=list(map(int,input().split()))
index=0
ans=0
while True:
    if List[index]==turn: ans+=1; turn=(turn+1)%3;
    index+=1
    if index==n: break
    
print(ans)