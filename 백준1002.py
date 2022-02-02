import math
t=int(input())

for i in range(t):
    x1,y1,r1,x2,y2,r2=map(int, input().split())

    d=(x2-x1)**2+(y2-y1)**2
    if (r2-r1)**2 < d < (r2+r1)**2:
        print(2)
    elif d==(r1+r2)**2:
        print(1)
    elif d==(r2-r1)**2 and d!=0:
        print(1)
    elif d<(r2-r1)**2 or d>(r1+r2)**2:
        print(0)
    elif d==0 and r1==r2:
        print(-1)
