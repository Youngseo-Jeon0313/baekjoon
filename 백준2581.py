n=10001
a = [True]*(n+1)


primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

M=int(input())
N=int(input())
List=[]
for i in range(M,N+1):
    for j in primes: 
       if i==j:
          List.append(i)

if len(List)==0: print(-1)
else:
   print(sum(List))
   print(List[0])