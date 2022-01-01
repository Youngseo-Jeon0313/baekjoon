def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>= m:
        return False
    #만약 현재 노드가 아직 방문하지 않은 노드라면
    if graph[x][y] == 0:
        #이렇게 방문처리 -> 1로 바꿔준다
        graph[x][y] = 1
        #상하좌우의 위치들도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

#N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)