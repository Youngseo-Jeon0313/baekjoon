A,B=map(int, input().split())
N=int(input())
M=list()
for i in range(N):
    M.append(int(input()))

M.append(A)

if A==B:
    print(0)
else:
    for i in range(N+1):
        M[i]=abs(M[i]-B)
    if min(M)==M[-1]:
        print(min(M))
    else:
        print(1+min(M))