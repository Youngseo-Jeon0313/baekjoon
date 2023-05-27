n=int(input())
a,b=0,0

for _ in range(n):
    x,y=map(int,input().split())
    if x>y: a+=1
    elif x<y: b+=1
print(a,b)