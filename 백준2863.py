a,b=map(int,input().split())
c,d=map(int,input().split())

SUM=0; ans=0
if SUM<a/c+b/d:ans=0; SUM=a/c+b/d
if SUM<c/d+a/b: ans=1; SUM=c/d+a/b
if SUM<d/b+c/a: ans=2; SUM=d/b+c/a
if SUM<b/a+d/c: ans=3; SUM=b/a+d/c
print(ans)