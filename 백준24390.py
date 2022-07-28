import sys
input=sys.stdin.readline

a,b=input().split(':') #a에는 분, b에는 초가 할당된다.
time=int(a)*60 + int(b)

min_button=float('inf')

def bfs(remain,button,arr):
    global min_button
    #min으로 
    #bfs간다
    #첫번째 방법: 
    if remain>0 :
        if remain-600>=0:
            bfs(remain-600,button+1,arr+[600])
        if remain-60>=0:
            bfs(remain-60,button+1,arr+[60])
        if remain-30>=0:
            bfs(remain-30, button+1,arr+[30])    
        if remain-10>=0:
            bfs(remain-10,button+1,arr+[10])
    if remain==0 :
        if 30 not in arr:
            min_button=button+1
        else:
            min_button=button
        print(min_button);exit();
   # print(remain,button,arr)

    
#10 30 60 600
bfs(time,0,[])
print(min_button)