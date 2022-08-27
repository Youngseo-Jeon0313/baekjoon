import sys
input=sys.stdin.readline

N=int(input())

ans=N
for i in range(1,N+1):
    ans+=2*i
print(ans)
for i in range(1,N+1):
    if i%2==1:
        for j in range(i):
            print('1',j+1)
    else:
        for j in range(i):
            print('2',j+1)
#print('아')

if N%2==0:
    for l in range(N):
        print('1', l+1)
if N%2==1:
    for l in range(N):
        print('2', l+1)

#print('우')
for i in range(N,0,-1):
    if i%2==0:
        for j in range(N-i,N):
            print('2',j+1)
    else:
        for j in range(N-i,N):
            print('1', j+1)
            