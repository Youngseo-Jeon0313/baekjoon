T=int(input())
for _ in range(T):
    n,x,y=map(int,input().split())
    if x==0 and y==0: print(-1)
    elif x>0 and y>0: print(-1)
    elif (n-1)%(x+y)!=0: print(-1)
    else:
        if x>0: x=x
        elif y>0: x=y
        index=1
        start=1
        while index<n:
            print(start,end=' ')
            if index%x==0: 
                if start==1:start+=(x+1)
                else: start+=x
            index+=1
        print()
