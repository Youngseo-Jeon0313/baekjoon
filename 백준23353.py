import sys
input=sys.stdin.readline

N=int(input())
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))

#DP 느낌
ans=[[0 for _ in range(N)]for _ in range(N)]


for i in range(N):
    for j in range(N):
        flag=False
        if arr[i][j]==1 or arr[i][j]==2:
            if ans[i][j]: flag=True
            check=0;tempans=0
            tempi=i; tempj=j
            while tempi<N and tempj<N and ((arr[tempi][tempj]==1 and check<=1) or (arr[tempi][tempj]==2 and check==0)):
                if arr[tempi][tempj]==2: check+=1
                tempans+=1;
                ans[tempi][tempj]=max(ans[tempi][tempj],tempans)
                tempi+=1; tempj-=1
            if flag==True: continue
            check=0; tempans=0
            tempi=i; tempj=j
            while tempi<N and tempj<N and ((arr[tempi][tempj]==1 and check<=1) or (arr[tempi][tempj]==2 and check==0)):
                if arr[tempi][tempj]==2: check+=1
                tempans+=1; 
                ans[tempi][tempj]=max(ans[tempi][tempj],tempans)
                tempi+=1; 
            check=0; tempans=0
            tempi=i; tempj=j
            while tempi<N and tempj<N and ((arr[tempi][tempj]==1 and check<=1) or (arr[tempi][tempj]==2 and check==0)):
                if arr[tempi][tempj]==2: check+=1
                tempans+=1; 
                ans[tempi][tempj]=max(ans[tempi][tempj],tempans)
                tempj+=1; 
            check=0;tempans=0
            tempi=i; tempj=j
            while tempi<N and tempj<N and ((arr[tempi][tempj]==1 and check<=1) or (arr[tempi][tempj]==2 and check==0)):
                if arr[tempi][tempj]==2: check+=1
                tempans+=1;
                ans[tempi][tempj]=max(ans[tempi][tempj],tempans)
                tempi+=1; tempj+=1
            
    
# print(ans)
ANS=0
for i in ans:
    ANS=max(ANS,max(i))
print(ANS)

'''
3
1 1 1
1 2 1
1 1 1
3

3
0 2 0
0 0 0
0 0 0
1

1
2
1

8
1 0 2 0 1 0 2 0
2 0 1 1 1 1 0 0
2 0 0 1 0 0 1 1
0 1 0 1 1 1 1 0
0 0 0 1 0 1 0 0
1 0 2 0 1 2 2 1
0 2 0 1 0 1 2 2
2 0 1 0 1 0 1 1
7
'''