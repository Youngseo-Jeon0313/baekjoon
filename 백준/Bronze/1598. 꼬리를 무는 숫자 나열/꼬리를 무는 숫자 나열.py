N,M=map(int,input().split())
N-=1; M-=1
if N>M: N,M=M,N
ans=(M//4-N//4)+abs(M%4-N%4)
print(ans)