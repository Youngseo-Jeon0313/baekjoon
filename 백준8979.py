M,N=map(int, input().split())

List=[]
for i in range(M):
    List.append(list(input().split()))

L=sorted(List, key=lambda x: [x[1],x[2],x[3]])

print(L[-N][0])