import sys
input=sys.stdin.readline

a,b,n,w=map(int,input().split())
if a-b!=0 and (w-b*n)/(a-b)==int((w-b*n)/(a-b)) and (w-b*n)/(a-b)>0:
    print(int(w-b*n)/(a-b), int(n-(w-b*n)/(a-b)))
elif a-b==0 and w-b*n==0:
    if n>2: print(-1)
    else:
        print(1,n-1)
else:
    print(-1)