'''
def go(check, start):
    if sum(check) == m:
        ans = [arr[i] for i in range(n) if check[i]]
        print(' '.join(map(str,ans)))
        return
    for i in range(start, n):
        if check[i] == 0:
            check[i] = 1
            go(check, i+1)
            check[i] = 0

n, m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
go([0]*n, 0)

'''
n, m = map(int, input().split())
my_list = list(map(int, input().split()))
my_list.sort()
visited = [False] * n
solve = []

def Dfs(depth):
    if m == depth:
        print(' '.join(map(str, solve)))
        return

    for i in range(n): 
        if not visited[i]:
            if depth == 0 or solve[depth - 1] < my_list[i]:
                solve.append(my_list[i])
                visited[i] = True
                #print(visited)
                print(solve)
                Dfs(depth + 1)
                visited[i] = False
                #print(visited)
                solve.pop()

Dfs(0)


