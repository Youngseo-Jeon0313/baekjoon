import sys
input=sys.stdin.readline
sys.setrecursionlimit(111111)

T=int(input())
#사이클 리스트를 슬라이딩하는 방법 사용!!

def dfs(node):
    global answer
    check[node]=1
    cycle.append(node)
    
    next=students[node]
    if check[next]:
        if next in cycle:
            answer+=cycle[cycle.index(next):]
        return
    else:
        dfs(next)

for _ in range(T):
    N=int(input())
    answer=[]
    check=[0 for _ in range(N+1)]
    students=list(map(int,input().split()))
    students=[0]+students
    for i in range(1,N+1):
        if not check[i]:
            cycle=[]
            dfs(i)
    
    print(N-len(answer))