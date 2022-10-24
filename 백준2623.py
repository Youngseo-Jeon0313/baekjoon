import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
indegree=[0]*(n+1)
time=[0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for i in range(1,n+1):
    List=list(map(int,input().split()))
    for j in range(len(List)):
        if List[j]==-1: break
        if j==0: time[i]+=List[j]
        else: indegree[i]+=1; graph[List[j]].append(i)

# print('indegree',indegree)
# print('graph',graph)


def topology_sort():
    result=[0 for _ in range(n+1)]
    queue=deque()
    for i in range(1,n+1):
        if indegree[i]==0:
            queue.append([i,time[i]])
    while queue:
        print(queue)
        current,current_time=queue.popleft()
        result[current]=max(result[current],current_time)
        for j in graph[current]:
            indegree[j]-=1
            result[j]=max(result[j],result[current]+time[j])
            if indegree[j]==0:
                queue.append([j,current_time+time[j]])

    for i in range(1,n+1):
        print(result[i])

topology_sort()

'''
5
10 -1
20 1 -1
30 2 -1
40 3 5 -1
100 -1

답
10 30 60 140 100

'''