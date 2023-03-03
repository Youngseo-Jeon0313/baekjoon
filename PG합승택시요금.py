from heapq import *
import sys
input=sys.stdin.

def solution(n, s, a, b, fares): 
    adj=[[] for _ in range(n+1)]
    for i in fares:
        adj[i[0]].append([i[1],i[2]]) #(연결되어있는 것, cost) 이렇게 저장
        adj[i[1]].append([i[0],i[2]])
    
    def dijkstra(start, distance):
        q=[]
        heappush(q,(0,start))
        distance[start]=0
        while q:
            dist,now=heappop(q)
            if dist>distance[now]: continue
            for i in adj[now]:
                if i[1]+dist<distance[i[0]]:
                    distance[i[0]]=i[1]+dist
                    heappush(q,(distance[i[0]],i[0]))
        return distance
    
    distance_s=dijkstra(s,[1000000 for _ in range(n+1)])
    distance_a=dijkstra(a,[1000000 for _ in range(n+1)])
    distance_b=dijkstra(b,[1000000 for _ in range(n+1)])
    answer = float('inf')
    for i in range(1,n+1):
        if distance_s[i]+distance_a[i]+distance_b[i]<answer:
            answer=distance_s[i]+distance_a[i]+distance_b[i]
    
    return answer