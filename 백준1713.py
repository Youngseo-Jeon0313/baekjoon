N=int(input())
M=int(input())
List=list(map(int,input().split()))

Picture=[[0,0,0] for _ in range(N)] #학생, 추천횟수
for i in range(M):
    flag=False
    for j in Picture:
        if j[0]==List[i] : 
            j[1]+=1
            flag=True
            break
        elif j[0]==0: 
            j[0]=List[i]; j[1]+=1; j[2]=i
            flag=True
            break
    if not flag:
        Picture=sorted(Picture, key = lambda x:[x[1], x[2]])
        Picture[0][0]=List[i]
        Picture[0][1]=1
        Picture[0][2]=i
    
    # print(Picture)
ans=[]
for i in Picture:
    if i[0]>0:
        ans.append(i[0])
ans=sorted(ans)
print(*ans)
