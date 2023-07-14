N,L,R,X = map(int,input().split())
Problem=list(map(int,input().split()))
ans=0

def backtracking(node, visited, List): 
    global ans
    List=sorted(List)
    if sum(List) >= L and sum(List) <= R and List[-1]-List[0] >= X: 
        # print(List)
        ans+=1 
        #return하면 안됨 . => 한 번 더 가야할 수도 있으니까
    for i in range(node+1, N): # 1 ~ N 까지
        if not visited[i]: # 중복 확인
            visited[i]=1
            backtracking(i, visited,List+[Problem[i]])
            visited[i]=0

visited=[0 for _ in range(N)]
backtracking(-1, visited, [])
print(ans)