import sys
input=sys.stdin.readline

n,m=map(int,input().split())

c1,c2=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort()
b.sort()

d=abs(c1-c2)
p1=0; p2=0;
ans=1
max=float('inf')
flag=1;
while p1<n and p2<m:
    # print('left', p1, 'right', p2, ans, max)
    if abs(b[p2]-a[p1])+d<max:
        ans=1; max=abs(b[p2]-a[p1])+d;
    elif abs(b[p2]-a[p1])+d==max:
        ans+=1; 
    if b[p2]>a[p1]: p1+=1
    else: p2+=1
print(max, ans)