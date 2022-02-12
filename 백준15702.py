N,M=map(int,input().split())
score=list(map(int,input().split()))
arr=list(list(input().split()) for _ in range(M))
MAX=0
best=[]
for i in range(M):
    total=0
    for j in range(1,N+1):
        if arr[i][j]=='O': 
            total+=score[j-1]
    if total>=MAX:
        MAX=total
    arr[i].append(total)

for i in range(M):
    if arr[i][N+1]==MAX:
        best.append(int(arr[i][0]))

best.sort()
print(best[0],MAX)

