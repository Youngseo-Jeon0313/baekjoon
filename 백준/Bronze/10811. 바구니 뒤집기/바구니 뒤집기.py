N,M=map(int,input().split())
List=[i for i in range(1,N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    temp = List[a-1:b]
    temp.reverse()
    List[a-1:b] = temp
print(*List)