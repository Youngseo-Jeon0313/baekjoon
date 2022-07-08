from collections import deque

C,L,leng=map(int,input().split())
road=[]
for _ in range(C): road.append(input())
dx,dy=[1,-1,0,0],[0,0,1,-1]
charac=input()
check=[[0 for _ in range(L)] for _ in range(C)] 
charac+='0'

sum=0;
before_x=0; before_y=0;
end_x=0; end_y=0;
totalans=[];

while True: #반복해서 charac이 있는지를 확인할 거다.
    #여기서부터는 이 단어 속에서 한 바퀴 돌 것을 생각해서 가져올 것임
    ans=[]
    flag=False #flag의 핵심은 '한 번이라도' 걸리면 break로 탈출시켜 버릴 것!!
    for i in charac:
        q=deque(); q.append([before_x,before_y])
        check_=[[0 for _ in range(L)] for _ in range(C)]
        flag_=False;
        if i=='0': flag_=True; #한바퀴는 끝났다.
        if flag_==False: #한 바퀴가 끝나지 않았을 경우
            while q:
                #그 단어 한 개를 현재 위치에서 최소 비용을 들여 찾을 것
                x,y=q[0]
                if road[x][y]==i and not check[x][y]: 
                    check[x][y]=True; flag_=True; break; #골랐다.
                else:
                    x,y=q.popleft()
                    for j in range(4):
                        nx=x+dx[j]; ny=y+dy[j]
                        if 0<=nx and nx<C and 0<=ny and ny<L and not check_[nx][ny] : q.append([nx,ny]); check_[nx][ny]=1
       
        if flag_==True: #찾았다면
            if i!='0':
                if x>before_x: ans.append('D'*(x-before_x)); before_x=x; 
                if x<before_x: ans.append('U'*(before_x-x)); before_x=x;
                if y>before_y: ans.append('R'*(y-before_y)); before_y=y;
                if y<before_y: ans.append('L'*(before_y-y)); before_y=y;
                ans.append('P')
        else: break
    if i=='0':
        flag=True; sum+=1; totalans.extend(ans)
        end_x=x; end_y=y;
    else: break;       
  

x,y=C-1,L-1
if x>end_x: totalans.append('D'*(x-end_x)); 
if x<end_x: totalans.append('U'*(end_x-x)); 
if y>end_y: totalans.append('R'*(y-end_y)); 
if y<end_y: totalans.append('L'*(end_y-y)); 


    
ans=''
for i in totalans:
    ans+=i

print(sum, len(ans))
print(ans,sep='')