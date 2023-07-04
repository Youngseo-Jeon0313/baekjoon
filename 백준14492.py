ans=0
N=int(input())
A=[]
B=[]
for _ in range(N):
    A.append(list(map(int,input().split())))
for _ in range(N):
    B.append(list(map(int,input().split())))
for i in range(N):
    for j in range(N):
        for k in range(N):
            if A[i][k]&B[k][j]: ans+=1; break;

print(ans)