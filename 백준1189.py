import sys
input=sys.stdin.readline

R,C,K=map(int,input().split())
List=[]
ans=0

for _ in range(R):
    List.append(list(input()))


def backtracking(row,col,cnt,visited):
    
    #print(row,col)
    global ans
    if row==0 and col==C-1 and cnt==K: ans+=1; return
    #위 또는 오른쪽으로 가는 거임
    if row-1>=0 and List[row-1][col]!='T' and [row-1,col] not in visited: backtracking(row-1,col,cnt+1,visited+[[row-1,col]])
    if col+1<C and List[row][col+1]!='T' and [row,col+1] not in visited: backtracking(row,col+1,cnt+1,visited+[[row,col+1]])
    if row+1<R and List[row+1][col]!='T' and [row+1, col] not in visited: backtracking(row+1,col,cnt+1,visited+[[row+1,col]])
    if col-1>=0 and List[row][col-1]!='T' and [row, col-1] not in visited: backtracking(row,col-1,cnt+1,visited+[[row,col-1]])

backtracking(R-1,0,1,[[R-1,0]])
print(ans)