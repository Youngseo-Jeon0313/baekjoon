def go(idx,num):
    global res
    if num == n//2:
        aTeam, bTeam = 0,0
        for i in range(n):
            for j in range(i+1,n):
                if team[i] ==team[j]:
                    if team[i] ==0: aTeam += arr[i][j]+ arr[j][i]
                    else: bTeam += arr[i][j] + arr[j][i]
        res = min(res,abs(aTeam-bTeam))

    for i in range(idx+1, n):
        team[i]=1
        go(i,num+1)
        team[i]=0

n=int(input())
arr=[[*map(int, input().split())]for _ in range(n)]
res = float('inf')
team = [0]*n
go(0,0)
print(res)