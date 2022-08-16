import sys
input=sys.stdin.readline

n=1000001
prime = [True]*(n+1)

for i in range(2,n+1):
  if prime[i]:
    for j in range(2*i, n+1, i):
        prime[j] = False

def check2(num):
    arr=[]
    ans=0
    while True:
        ans=0
        while num!=0:
            ans+=(num%10)**2
            num//=10
        if ans in arr: return 0;
        if ans==1:  return 1
        arr.append(ans)
        #print(arr)
        num=ans
        


N=int(input())
for i in range(2,N+1):
    if prime[i] and check2(i): print(i)





