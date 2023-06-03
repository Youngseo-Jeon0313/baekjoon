
N=int(input())
S=input()
List=[0,0,0] #대각선 #오른쪽 #위쪽
for i in S:
    if i=='U': List[2]+=1
    elif i=='X': List[0]+=1
    else: List[1]+=1
T=int(input())
ans=0
for _ in range(T):
    x,y=map(int,input().split())
    x-=1; y-=1
    flag=True
    MIN=min(x,y)
    if MIN>=List[0]: x-=List[0];  y-=List[0]
    else: x-=MIN; y-=MIN;
    if x>List[1]: flag=False
    if y>List[2]: flag=False
    if flag: ans+=1; 
    # print('아',x,y)

print(ans)