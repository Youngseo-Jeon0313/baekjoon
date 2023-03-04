from collections import deque
dx, dy= [1,-1,0,0],[0,0,1,-1]
arr=list(list(input())for _ in range(12))
Ans=0

def check(x,y):
    if 0<=x<12 and 0<=y<6: return True
    return False

while True:
   ans=0
   check_arr=[[0]*6 for _ in range(12)]
   for i in range(12):
       for j in range(6):
           check_arr[i][j]=1
           if arr[i][j]!='.':
               q=deque()
               pung_q=deque()
               pung_q.append((i,j))
               q.append((i,j))
               while q:
                  x,y=q.popleft()
                  for k in range(4):
                      nx,ny=x+dx[k],y+dy[k]
                      if check(nx,ny) and arr[nx][ny]==arr[x][y] and check_arr[nx][ny]==0:
                          pung_q.append((nx,ny))
                          q.append((nx,ny))
                          check_arr[nx][ny]=1
               if len(pung_q)>=4:
                   ans+=1
                   for (i,j) in pung_q: arr[i][j]='.'
   if ans==0: break 
   Ans+=1
   
   for i in range(11):
       for j in range(11):
           for k in range(6):
               if arr[j][k]!='.' and arr[j+1][k]=='.':
                   arr[j][k], arr[j+1][k]='.', arr[j][k]

   
print(Ans)
