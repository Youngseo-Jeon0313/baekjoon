'''
모든 지점에서 모든 지점까지의 거리!
think
어딜 거쳐서 가면 더 빠르다고??
'''
def FloydWarshall(G):
    n = len(G)
    dist = list(G)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (dist[i][j] > dist[i][k] + dist[k][j]):
                    dist[i][j] = dist[j][k] + dist[k][j]
    return dist

G=[[0,float('inf'),-2,float('inf')],[4,0,3,float('inf')],[float('inf'),float('inf'),0,2],[float('inf'),-1,float('inf'),0]]
print(FloydWarshall(G))