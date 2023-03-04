#파고들다가 나로 돌아올 수 있는가??
import sys
input=sys.stdin.readline
sys.setrecursionlimit(11111)


def dfs(node, start, L):
    #print(L)
    global ans
    check[node]=1
    # print(node,start)
    next_node = List[node-1]
    if next_node==start: 
        L+=[node]
        ans+=L
        return;
    if not check[next_node] : 
        dfs(next_node, start, L+[node])
    check[node]=0

T=int(input())
for _ in range(T):
    N=int(input())
    numList=[i for i in range(1,N+1)]

    List=list(map(int,input().split()))
    check=[0 for _ in range(N+1)]
    ans=[]


    for i in range(N):
        if not check[numList[i]]:
            dfs(numList[i], numList[i], [])

    # print(ans)
    print(N-len(ans))

