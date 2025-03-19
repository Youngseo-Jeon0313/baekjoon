import sys
sys.setrecursionlimit(300000)

'''
끝에 도달하면 ? -> 자기를 0으로 만들기 위해 부모에게 자기를 더해야 함.
그럼 각각의 노드는 무엇을 반환해야 해? -> 자신의 값을 반환
정답은 그 반환하는 전체 횟수가 중요함 -> abs(더하거나 빼는 행위의 값)

'''

answer = 0
def solution(a, edges):
    global answer
    if sum(a)!=0: return -1
    adj = [[] for _ in range(len(a))]
    for i in edges:
        adj[i[0]].append(i[1])
        adj[i[1]].append(i[0])
    visited = [0 for _ in range(len(a))]
    
    def dfs(node):
        global answer
        visited[node]=1
        temp = 0
        for i in adj[node]:
            if not visited[i]:   
                check = dfs(i)
                a[node]+=check
                answer+=abs(check)
                #print(check)
                
        return a[node]
    
    #print(a)
    dfs(0)
    return answer