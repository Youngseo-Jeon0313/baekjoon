t=int(input())
for _ in range(t):
    l,r,x=map(int,input().split())
    a,b=map(int,input().split())
    if a==b: print(0)
    elif (a<b and a+x<=b) or (a>b and a-x>=b): print(1)
    elif a+x>=r and a-x<=l: print(-1)
    elif a<b and (b+x<=r or a-x>=l) : print(2)
    elif a>b and (a+x<=r or b-x>=l): print(2)
    else: print(3)