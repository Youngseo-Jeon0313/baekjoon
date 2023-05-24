'''N=int(input())
for i in range(N,0,-1):
    print('*'*((N-i)),' '*(2*i),'*'*((N-i)),sep='')
print('*'*(2*N))
for i in range(1,N+1):
    print('*'*((N-i)),' '*(2*i),'*'*((N-i)),sep='')'''

n = int(input())
for i in range(1, n):
    print('*'*i + ' '*2*(n-i) + '*'*i)
for i in range(n, 0, -1):
    print('*'*i + ' '*2*(n-i) + '*'*i)