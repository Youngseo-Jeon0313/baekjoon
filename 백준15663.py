n, m = map(int, input().split())
my_list = list(map(int, input().split()))
my_list.sort()
visited = [False] * n
solve = []
Ans=[]

def Dfs(depth):
    if m == depth:
        a=' '.join(map(str, solve))
        if a not in Ans:
            Ans.append(a)
        return
    for i in range(n): 
        if not visited[i]:
                solve.append(my_list[i])
                visited[i] = True
                Dfs(depth + 1)
                visited[i] = False
                solve.pop()

Dfs(0)

for i in Ans:
    print(i)

