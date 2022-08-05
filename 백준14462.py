N=int(input())
Left=[]
Right=[]
for _ in range(N):
    Left.append(int(input()))
for _ in range(N):
    Right.append(int(input()))
Left=[0]+Left
Right=[0]+Right
DP=[[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        if abs(Left[i]-Right[j]) <=4  :
            #갈 수 있다.
            DP[i][j]=max(DP[i-1][j-1]+1,DP[i][j-1])
        else:
            #갈 수 없다. 안 간다.
            DP[i][j]=max(DP[i][j-1],DP[i-1][j])
        
# print(DP)

print(max(DP[N]))