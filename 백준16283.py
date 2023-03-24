a,b,n,w=map(int,input().split())
answer=[]
flag=False
for i in range(1,1001):
    for j in range(1,1001):
        if a*i+b*j==w and i+j==n:
            if answer: 
                flag=False
            else: 
                flag=True
                answer=[i,j]
if flag:
    print(*answer)
else:
    print(-1)