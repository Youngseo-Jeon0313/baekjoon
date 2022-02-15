from collections import deque

def bfs():
    q=deque() #floodfill을 위한 변수
    q.append(Subin)
    while q:
        x=q.popleft()
        if x==Sister: print(arr[x]); exit()
        for nx in (x-1,x+1,2*x):
            if 0<=nx<=100000*2+1 and not arr[nx]:
                arr[nx]=arr[x]+1
                q.append(nx)
#배열 만들기
arr=[0]*(100000*2+2)
Subin,Sister=map(int,input().split())


bfs()