N=int(input())
List=[]
for i in range(N):x=int(input()); List.append(x)
Graph=['' for _ in range(N+1)]
for j in range(N-1):
    x,y,z=input().split()
    List.append([x,y,z])

#일단 트리를 만든다.

def bfs(nodenum,nodeval, l,r):
    Graph[nodenum]=nodeval
    if len(List[l])==3: 
        bfs(l,List[l][0],List[l][1],List[l][2])
        bfs(r,List[r][0],List[r][1],List[r][2])





rootnode,l,r=List[-1]
bfs(1,rootnode,l,r)
print(Graph)