'''
이분매칭
'''


def dfs(x):
  for i in cow[x]:
    if check[i]:
      continue
    check[i]=True  
    if visited[i] == -1 or dfs(visited[i]):   #축사에 소가 없거나 
      visited[i]= x                           #축사에 들어있는 소를 밀어낼 수 있으면 True
      return True
  return False 

n,m=map(int, input().split())
cow = [[] for _ in range(n)]
visited=[-1]*m
result=0

for i in range(n):
  a=list(map(int, input().split()))
  for j in a[1:]:
    j=j-1
    cow[i].append(j)

for i in range(n):
  check=[False]*m
  if dfs(i):
    result +=1

print(result)