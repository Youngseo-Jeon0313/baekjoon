t=int(input())

while t:
    t-=1
    N,M=map(int, input().split())
    U=2*M -N
    T=M-U
    print(U,T)