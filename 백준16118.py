import sys
input=sys.stdin.readline
from heapq import *
def dijkstra_fox(start): #일정
    fox[start]=0
    fox_hq=[]
    heappush(fox_hq, [start,0,1]) #위치, 점수, 스텝
    while fox_hq:
        pos, score, step = heappop(fox_hq)
        if fox[pos]<score:continue
        for i in Road[pos]:
            next=i[0]; cost=i[1]
            if score+cost < fox[next]:
                fox[next]=score+cost
                heappush(fox_hq,[next,fox[next],step+1])


def dijkstra_wolf(start):
    wolf[1][start]=0
    wolf_hq=[]
    heappush(wolf_hq,[start,0,0]) #장소, 점수, 스텝
    while wolf_hq:
        pos, score, step = heappop(wolf_hq)
        if step%2 and wolf[0][pos]<score: continue
        elif step%2==0 and wolf[1][pos]<score: continue
        for i in Road[pos]:
            next=i[0]; cost=i[1]
            if step%2:
                if score+cost*2 < wolf[1][next]:
                    wolf[1][next]=score+cost*2
                    heappush(wolf_hq,[next,wolf[1][next],step+1])
            else:
                if score+cost//2 < wolf[0][next]:
                    wolf[0][next]=score+cost//2
                    heappush(wolf_hq,[next,wolf[0][next],step+1])            

N,M = map(int,input().split())
fox=[float('inf') for _ in range(N+1)]
wolf=[[float('inf') for _ in range(N+1)] for _ in range(2)]

Road = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,d=map(int,input().split())
    Road[a].append((b,2*d))
    Road[b].append((a,2*d))

dijkstra_fox(1)
dijkstra_wolf(1)

# print(fox)
# print(wolf)

ans=0
for i in range(1,N+1):
    if fox[i]<min(wolf[0][i],wolf[1][i]): ans+=1

print(ans)