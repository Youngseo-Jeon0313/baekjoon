'''
(psum[r2][c2]-psum[r2][c1-1]-psum[r1-1][c2]+psum[r1-1][c1-1])//((r2-r1+1)*(c2-c1+1))
'''
from itertools import combinations as cb
R,C=map(int,input().split())

if R==1: 
    MAX_1=0
    arr=list(map(int,input()))
    psum_1=[0 for _ in range(C)]
    psum_1[0]=arr[0]
    for i in range(1,C):
        psum_1[i]=psum_1[i-1]+arr[i]
    for x in cb(list(i for i in range(C-1)),2):
        MAX_1=max(MAX_1, (psum_1[-1]-psum_1[x[1]])*(psum_1[x[1]]-psum_1[x[0]])*psum_1[x[0]])
    print(MAX_1);

elif C==1:
    MAX_1=0
    R,C=C,R
    arr=[]
    for i in range(C): arr.append(int(input()))
    psum_1=[0 for _ in range(C)]
    psum_1[0]=arr[0]
    for i in range(1,C):
        psum_1[i]=psum_1[i-1]+arr[i]
    for x in cb([i for i in range(C-1)],2):
        MAX_1=max(MAX_1, (psum_1[-1]-psum_1[x[1]])*(psum_1[x[1]]-psum_1[x[0]])*psum_1[x[0]])
    print(MAX_1);
    


else:
    arr = [list(map(int,input())) for _ in range(R)]
    psum=[[0]*(C+1) for _ in range(R+1)]
    for i in range(1, R+1):
        for j in range(1, C+1):
            psum[i][j]=psum[i-1][j]+psum[i][j-1]-psum[i-1][j-1]+arr[i-1][j-1]
    
    MAX=0
    for x in cb([i for i in range(1,C)],2):
        MAX=max(MAX,(psum[R][C]-psum[R][x[1]])*(psum[R][x[1]]-psum[R][x[0]])*psum[R][x[0]])
    for y in cb([i for i in range(R-1)],2):
        MAX=max(MAX,(psum[R][C]-psum[y[1]][C])*(psum[y[1]][C]-psum[y[0]][C])*psum[y[0]][C])

    for i in range(1,R+1):
        for j in range(1,C+1):
            if i==R and j==C: continue
            elif i==R: 
                firstbox=psum[R][j]
                for k in range(1,R):
                    secondbox=(psum[k][C]-psum[k][j])
                    thirdbox=psum[R][C]-firstbox-secondbox
                    MAX=max(MAX,firstbox*secondbox*thirdbox)
                
            elif j==C: 
                firstbox=psum[i][j]
                for k in range(1,C):
                    secondbox=(psum[R][k]-psum[i][k])
                    thirdbox=psum[R][C]-firstbox-secondbox
                    MAX=max(MAX,firstbox*secondbox*thirdbox)
            else: 
                firstbox=psum[i][j]
                secondbox=psum[R][j]-psum[i][j]
                thirdbox=psum[R][C]-firstbox-secondbox
                MAX=max(MAX,firstbox*secondbox*thirdbox)
                secondbox=psum[i][C]-psum[i][j]
                thirdbox=psum[R][C]-firstbox-secondbox
                MAX=max(MAX,firstbox*secondbox*thirdbox)
    print(MAX)