MOD = 10**9 + 7

n = int(input())
s = input()

arr = [[0] * 4 for _ in range(n+1)] # 0: W, 1: WH, 2: WHE, 3:WHEE~~
for i in range(n):
    for j in range(4):
        arr[i+1][j] = arr[i][j]
    if s[i] == 'W': arr[i+1][0] += 1
    if s[i] == 'H': arr[i+1][1] += arr[i][0]
    if s[i] == 'E':
        arr[i+1][2] += arr[i][1]
        arr[i+1][3] += arr[i][2] + arr[i][3]
    for j in range(4):
        arr[i+1][j] %= MOD
print(arr[-1][3])