'''
r1,c1,r2,c2=map(int,input().split())

x,y -> 좌표
n -> 소용돌이 칠 것의 크기
arr -> 소용돌이 쳐서 만들 배열

def circle(x,y,n,arr):
    temp_x=x; temp_y=y
    #위로 올라가는 것
    index=(n-2)**2+1
    for i in range(n-1):
        temp_y-=1;
        arr[temp_x][temp_y]=index
        index+=1
    for i in range(n-1):
        temp_x-=1; 
        arr[temp_x][temp_y]=index
        index+=1
    for i in range(n-1):
        temp_y+=1; 
        arr[temp_x][temp_y]=index
        index+=1
    for i in range(n-1):
        temp_x+=1;
        arr[temp_x][temp_y]=index
        index+=1
    if n<10000: circle(x+1,y,n+2,arr)



# 배열 init
#-5000 ~ 5000 까지의 x와 y축을 가짐
List=[[0 for _ in range(10000+1)] for _ in range(10000+1)]
List[5000][5000]=1

circle(5001,5000,3,List)
for i in range(r1+5000, r2+5000+1):
    for j in range(c1+5000, c2+5000+1):
        print(List[i][j], end=' ')
    print()
    
'''

#각 x,y 좌표의 값을 구한다.
def get_value(x,y):
    idx=max(abs(x),abs(y))
    before_base = (2*(idx-1)+1)**2
    base = (2*idx+1)**2
    dx, dy = idx-x, idx-y

    if x>=y:
        return base-dx-dy
    else:
        return before_base+dx+dy
    
r1,c1,r2,c2=map(int,input().split())
arr =[]
for i in range(r1, r2+1):
    temp=[]
    for j in range(c1, c2+1):
        temp.append(get_value(i,j))
    arr.append(temp)

max_value = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        max_value = max(max_value, arr[i][j])

for i in range(len(arr)):
    for j in range(len(arr[i])):
        sub = len(str(max_value))-len(str(arr[i][j]))
        if sub>0:
            print(' '*sub, end='')
        print(arr[i][j], end=' ')
    print('')