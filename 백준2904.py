import sys
input=sys.stdin.readline

import math


n=1000001
a = [True]*(n+1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

N=int(input())
List=list(map(int,input().split()))
primegroup=[[0 for _ in range(N)] for _ in range(len(primes))]
#primegroup[어떤 수][소수가]=몇개 --> 예를 들면 primegroup[3번째 수, 8][2, 즉 primes인덱스1]=3
for i in range(len(List)):
    for j in range(len(primes)):
        if List[i]%primes[j]==0:
            while (List[i]%primes[j]==0):
                primegroup[j][i]+=1
                List[i]//=primes[j]

#print(primegroup)

ans1=1; ans2=0
for x in range(len(primes)):
    target=sum(primegroup[x])//N
    ans1*=primes[x]**int(target)
    for j in range(N):
        if target>primegroup[x][j]:
            ans2+=primegroup[x][j]-target
    # print(ans1, ans2)

# print(primegroup)

print(ans1, abs(int(ans2)))

