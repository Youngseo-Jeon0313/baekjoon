'''
dfs(x) : x(i번째 소) 번호 소가 들어갈 축사를 찾는 함수
True = 안착할 축소를 찾음 / False - 못찾음
check[i] : 해당 소x가 해당 축사(i)를 거쳤는지 체크
visited[i] : i번째 축사에 어떤 소가 있는지
'''


def dfs(x):
  for i in cow[x]:
    if check[i]:
      continue
    check[i]=True  
    # 재귀적으로 모두 만족되어야만 visited[i]=x로 할당됨
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