import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    n,q=map(int,input().split())
    dict={}
    for _ in range(n):
        x,y=map(int,input().split())
        if x*y in dict.keys():
            dict[x*y].append([x,y])
        else: dict[x*y]=[[x,y]]

    for _ in range(q):
        ans=0
        hs,ws,hb,wb=map(int,input().split())
        for i in dict.keys():
            if i>hs*ws and i<hb*wb:
                for dot in dict[i]:
                    i=dot[0];j=dot[1]
                    if i>hs and j>ws and i<hb and j<wb:
                        ans+=i*j
        print(ans)