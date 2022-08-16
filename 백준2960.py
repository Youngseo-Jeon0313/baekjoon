import sys
input=sys.stdin.readline

N,K=map(int,input().split())

a =[True] * (N + 1)
primes=[]
sum=0
for i in range(2,N+1):
  if a[i]:
    primes.append(i); sum+=1; 
    if sum==K: print(i)
    for j in range(i+i, N+1, i):
        if a[j]:
          a[j] = False; sum+=1;
          if sum==K: print(j)
    
