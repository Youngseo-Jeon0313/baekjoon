L,C= map(int, input().split())
my_list = list((input().split()))
my_list.sort()
visited = [False] * C
solve = []

def check(arr):
    jaeum=['a','e','i','o','u']
    moeum=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    flag1=False
    for i in arr:
        if i in jaeum:
            flag1=True
            break
    flag2=0
    for j in arr:
        if j in moeum:
            flag2+=1
            if flag2==2:
                break
    if flag1==True and flag2==2:
        return True
                
        
        
def Dfs(depth):
    if L == depth:
        if check(solve):
            print(''.join(solve))
            return
    for i in range(C):
        if not visited[i]:
            if depth == 0 or solve[depth - 1] < my_list[i]:
                solve.append(my_list[i])
                visited[i] = True
                Dfs(depth + 1)
                visited[i] = False
                solve.pop()
Dfs(0)