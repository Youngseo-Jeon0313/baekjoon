import math

N,M=input().split(':')
N=int(N); M=int(M)
for i in range(int(math.sqrt(M))+1,0,-1):
    a=M//i
    if a==0: continue
    if N%a==0 and M%a==0:
        N=N//a; M=M//a

    if N%i==0 and M%i==0:
        N=N//i; M=M//i

print(N//i,':',M//i,sep='')