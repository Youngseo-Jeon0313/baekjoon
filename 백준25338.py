import sys
input=sys.stdin.readline

a,b,c,d=map(int,input().split())
n=int(input())
sum=0
for _ in range(n):
    x,y=map(int,input().split())
    if max(a*(y-b)**2+c,d)==x: sum+=1
print(sum)