M,N=map(int,input().split())
Weight=[]
for _ in range(M):
    Weight.append(list(input()))

Store=[[0 for _ in range(N)] for _ in range(M)]
Print=[[0 for _ in range(N)] for _ in range(M)]
# print(Store)
for i in range(M):
    Print[i][0]=int(Weight[i][0])

for j in range(1,N):
    for i in range(M):
        if i>0:
            Store[i][j]=max(Print[i][j],Print[i-1][j-1])
        Store[i][j]=max(Print[i][j],Print[i][j-1])
        if i<N-2:
            Store[i][j]=max(Print[i][j],Print[i+1][j-1]) 
        Print[i][j]=Store[i][j]+int(Weight[i][j] )   
    # print('스토어',Store)
    # print("프린트", Print)
    
ans=0
for i in range(M):
    ans=max(ans,max(*Store[i]))

print(ans)