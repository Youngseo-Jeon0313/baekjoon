N,M=map(int,input().split())
list=[0 for _ in range(N)]
for _ in range(M):
    i,j,k=map(int,input().split())
    for box in range(i-1,j):
        list[box]=k
print(*list)