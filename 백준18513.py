import heapq
import sys
input=sys.stdin.readline
N,K=map(int,input().split())
Restroom=list(map(int,input().split()))
pos={}
for i in Restroom:
    pos[i]=0
'''
뭔가 그리디 하게 모든 그 Restroom에 가깝게 위치시킨다.
1,2,3,4 Restroom이 있으면 일단 최대한 가까운 위치에 설치
heap??

'''

#heap에 넣는다. 각 장소까지의 거리,현재 위치
heap=[]
heapq.heapify(heap)
ans=0
for i in Restroom:
    if i+1 not in pos: heapq.heappush(heap,[1,i+1]); K-=1;pos[i+1]=0;ans+=1
    if K==0: break;
    if i-1 not in pos: heapq.heappush(heap,[1,i-1]); K-=1;pos[i-1]=0; ans+=1
    if K==0: break;
if K==0: print(ans); exit()
while True:
    x,y=heapq.heappop(heap)
    if y+1 not in pos:heapq.heappush(heap,[x+1,y+1]); K-=1; ans+=(x+1); pos[y+1]=0
    if K==0: break;
    if y-1 not in pos:heapq.heappush(heap,[x+1,y-1]); K-=1; ans+=(x+1); pos[y-1]=0
    if K==0: break;

print(ans)


