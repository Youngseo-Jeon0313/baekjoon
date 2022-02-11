'''
종수의 움직임이 맨 밑에 주어진다.
한번씩 종수(I)가 움직일 때마다 아두이노들도 움직인다.
이 때 아두이노들은 종수와 가장 가까운 방향으로(5를 제외하고)
abs((종수x-자기x)+(종수y-자기y))
종수와 같은 위치에 있게 되는가?를 계속 물어봄
-맞으면 지게되고 krag 출력-틀리면 다음 움직임 시작

이게 R로 해서 하면 안되고ㅠㅠ 숫자로 표현해야 함
'''
from collections import deque
#방향키 조작
dr,dc=[1,1,1,0,0,0,-1,-1,-1],[-1,0,1,-1,0,1,-1,0,1]

N,M=map(int, input().split())
#바둑판의 상황을 2차원으로 저장한다.
arr=[list(input()) for _ in range(N)]
#바둑판 속 종수와 아두이노의 위치를 각각 넣는다.
R_directions=deque()
#종수의 움직임을 하나의 문자열로 넣는다.
J_movements = input() 
turn=0
#종수의 움직임을 하나씩 꺼내면서 진행시킨다.
for J_movement in J_movements:
    for i in range(N):
        for j in range(M):
            if arr[i][j]=='I':
                J_direction=[i,j]
            if arr[i][j]=='R':
                R_directions.append((i,j))
    turn+=1
    arr[J_direction[0]][J_direction[1]]='.'
    J_direction[0]+=dr[int(J_movement)-1]
    J_direction[1]+=dc[int(J_movement)-1]
    if arr[J_direction[0]][J_direction[1]]=='R': print('kraj',turn); exit();
    arr[J_direction[0]][J_direction[1]]='I'
    #종수가 한 번 움직일 때마다 R이 어떻게 움직여야 하는지??
    check=[[0]*M for _ in range(N)] #왔다감 표시용
    while (R_directions):
        #자 하나씩 체크를 하는데
        min_length=201
        x,y=R_directions.popleft()
        for i in range(9):
            if 0<=x+dr[i]<N and 0<=y+dc[i]<M:
                length=abs(x+dr[i]-J_direction[0])+abs(y+dc[i]-J_direction[1])
                if length<min_length: where=i; min_length=length
        arr[x][y]='.'
        if arr[x+dr[where]][y+dc[where]]=='I': print('kraj',turn); exit()
        #R이나 .일 경우
            #누군가 여기 한 번왔다? .으로 바꾸고 
        check[x+dr[where]][y+dc[where]]+=1
    for i in range(N):
        for j in range(M):
            if check[i][j]>1:
                arr[i][j]='.'
            if check[i][j]==1:
                arr[i][j]='R'               
                
for i in range(N):
    print(''.join(arr[i]))
