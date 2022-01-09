N=int(input())
mine=int(input())


#일단 만든다
myList= [[0 for col in range(N)] for row in range(N)]
'''
왼쪽, 오른쪽, 위, 아래 를 각각 배열로 나타낸 다음에
그걸 이용해서 달팽이를 계속 이동시키기!
'''
#달팽이가 갈 수 있는 곳
#~할 때 까지!



a=N*N

myList[0][0]=a


#위치 변동
x=0
y=0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
nx=0     
ny=0

#여기에 포문이 들어가야 되는디..
for i in range(3):
    for j in range(N-1):
        a-=1
        x+=dx[i]
        y+=dy[i]
        myList[x][y] = a
for k in range(N-2,0,-1): # 5 4 3 2 1 
    if k%2!=0:
        move1=[3,0]
        for i in move1:
            for j in range(k):
                a-=1
                x+=dx[i]
                y+=dy[i]
                myList[x][y] = a
    else:
        for i in range(1,3): #두번을 이 방법으로
            for j in range(k): #
                a-=1
                x+=dx[i]
                y+=dy[i]
                myList[x][y] = a

    
for i in range(N):
    for j in range(N):
        print (myList[i][j],end=' ')
    print( )
    
for i in range(N):
    for j in range(N):
        if myList[i][j]==mine:
            print(i+1,j+1)
