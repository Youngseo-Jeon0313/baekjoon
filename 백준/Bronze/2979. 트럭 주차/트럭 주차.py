ans=0
A,B,C=map(int,input().split())
List=[0 for _ in range(101)]
for _ in range(3):
    a,b=map(int,input().split())
    for i in range(a,b): List[i]+=1
# print(List)
for i in List:
    if i==1:ans+=A
    elif i==2: ans+=2*B
    elif i==3: ans+=3*C
print(ans)