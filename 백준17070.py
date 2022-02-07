import sys
input=sys.stdin.readline


def check(x, y):
    if 0 <= x < n and 0 <= y < n and arr[x][y] == 0: return True
    else: return False

def go(x, y, z):
    global ans
    if x == n-1 and y == n-1:
        ans += 1
        return
    if z == 1:
        if check(x, y+1): go(x, y+1, 1)
        if check(x, y+1) and check(x+1, y) and check(x+1, y+1):
            go(x+1, y+1, 2)
    elif z == 2:
        if check(x, y+1): go(x, y+1, 1)
        if check(x, y+1) and check(x+1, y) and check(x+1, y+1):
            go(x+1, y+1, 2)
        if check(x+1, y): go(x+1, y, 3)
    else:
        if check(x, y+1) and check(x+1, y) and check(x+1, y+1):
            go(x+1, y+1, 2)
        if check(x+1, y): go(x+1, y, 3)

n = int(input())
arr = list(list(map(int,input().split())) for _ in range(n))
ans = 0
go(0, 1, 1)
print(ans)