from heapq import *
hhh=[]
def solution(n, paths, gates, summits):
    adj=[[] for _ in range(n+1)]
    for i in range(len(paths)):
        s,e,t=paths[i]
        adj[s].append([t,e])
        adj[e].append([t,s])

    for gate in gates:
        check=[0 for _ in range(n+1)]
        hq=[[0,gate]]
    
        while hq:
            value,road = heappop(hq)
            check[road]=1
            if road in summits: heappush(hhh,[value, road]); break;
            for v, r in adj[road]:
                    if not check[r]:
                        heappush(hq, [max(value,v),r])    
    a=heappop(hhh)
    return a[1],a[0]

print(solution(6,[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],[1, 3],[5]))
# 5,3
print(solution(7,[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],	[1],	[2, 3, 4]	))
# 3,4
print(solution(7,[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],	[3, 7],	[1, 5]))
# 5,1