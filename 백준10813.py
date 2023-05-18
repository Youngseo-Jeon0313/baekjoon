N,M=map(int,input().split())
List=[i+1 for i in range(N)]
for _ in range(M):
    i,j=map(int,input().split())
    List[i-1],List[j-1]=List[j-1],List[i-1]
print(*List)