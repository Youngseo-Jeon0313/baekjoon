from collections import deque

def solution(n, edge):
    depth_list=[0 for _ in range(n+1)]
    adj=[[] for _ in range(n+1)]
    answer=0
    for i in edge:
        a,b=i[0],i[1]
        adj[a].append(b)
        adj[b].append(a)
    deq=deque([[1,1]])
    depth_list[1]=1
    while deq:
        node, depth=deq.popleft()
        for j in adj[node]:
            if not depth_list[j]: 
                depth_list[j]=depth+1
                deq.append([j,depth+1])
    # print(depth_list)                
    for k in range(n+1):
        if depth_list[k]==max(depth_list): answer+=1

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))