import sys
input=sys.stdin.readline

n=10000000
A,B=map(int,input().split())

a = [True]*(n+1)

primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

ans=0
for i in primes:
    res = i*i
    while True:
       if res<A: res*=i; continue
       if res>B: break;
       res*=i
       ans+=1
        
print(ans)