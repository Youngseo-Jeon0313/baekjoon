'''
큐나 덱을 이용해야 하는 이유
지렁이의 얼굴과 꼬리를 생각해보면 방향을 바꾸면서 
머리는 돌려지지만 꼬리는 안돌ㄹㅕ지자나
'''
from collections import deque

N=int(input())
K=int(input())
List=[[0 for _ in range(N+1)] for _ in range(N+1)] 
for _ in range(K):
    a,b=map(int,input().split())
    List[a][b]=1
L=int(input())
Direction=['' for _ in range(10**4)]
Directionkey=[[0,1],[1,0],[0,-1],[-1,0]]
for _ in range(L):
    when,how=input().split()
    Direction[int(when)]=how
time=0;direction=0; deq=deque()
deq.append([1,1])
dx,dy=Directionkey[direction][0],Directionkey[direction][1]
while True:
    time+=1
    if Direction[time-1]=='L':
            direction=(direction+3)%4
            dx,dy=Directionkey[direction][0],Directionkey[direction][1]
    elif Direction[time-1]=='D':
            direction=(direction+1)%4
            dx,dy=Directionkey[direction][0],Directionkey[direction][1]
    x,y=deq[-1]
    if [x+dx,y+dy] in deq: print(time); break;
    deq.append([x+dx,y+dy])
    if deq[-1][0]==0 or deq[-1][1]==0 or deq[-1][0]==N+1 or deq[-1][1]==N+1 : print(time); break;
    if len(deq)>1 and List[x+dx][y+dy]==0:
        deq.popleft()
    if List[x+dx][y+dy]==1: List[x+dx][y+dy]=0
