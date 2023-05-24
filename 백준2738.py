N,M=map(int,input().split())
List1=[]
List2=[]

for _ in range(N):
    List1.append(list(map(int,input().split())))

for _ in range(N):
    List2.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        print(List1[i][j]+List2[i][j], end=' ')
    print()