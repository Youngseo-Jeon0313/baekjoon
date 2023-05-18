T=int(input())
for _ in range(T):
    ans=0
    x1,y1,x2,y2=map(int,input().split())
    n=int(input())
    for _ in range(n):
        cx,cy,r=map(int,input().split())
        #하나는 안에 있고 하나는 밖에 있으면 
        if (cx-x1)**2+(cy-y1)**2<=r**2 and (cx-x2)**2+(cy-y2)**2>=r**2: ans+=1
        elif (cx-x1)**2+(cy-y1)**2>=r**2 and (cx-x2)**2+(cy-y2)**2<=r**2: ans+=1
    print(ans)