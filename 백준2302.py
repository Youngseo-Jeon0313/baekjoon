import sys
input=sys.stdin.readline

N=int(input())
M=int(input())

fibo = [0 for _ in range(41)]

fibo[0]=1
fibo[1]=1
fibo[2]=2
for i in range(3,41):
        fibo[i]=fibo[i-1]+fibo[i-2]
        
L=[(i+1) for i in range(M)]
no=[]
for _ in range(M):
    x=int(input())
    no.append(x)
ans=1


if M>0:
    flag=0
    for i in range(1,N+1):
        if (i in no) :
            ans*=fibo[i-1-flag]
            flag=i
    ans*=fibo[i-flag]
else:
    ans=fibo[N]

print(ans)