from itertools import combinations as cb

n, m = map(int,input().split())
arr = list(list(map(int,input().split())) for _ in range(n))
ans = float('inf')

Chicken = []
Home = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2: Chicken.append((i,j))
        if arr[i][j] == 1: Home.append((i,j))

choice = cb(Chicken, m)

print(list(choice))
'''


for choice_chicken in choice:
    res = 0
    for hx, hy in Home:
        dist = float('inf')
        for cx, cy in choice_chicken:
            dist = min(dist, abs(hx - cx) + abs(hy - cy))
        res += dist
    ans = min(ans, res)
print(ans)
'''