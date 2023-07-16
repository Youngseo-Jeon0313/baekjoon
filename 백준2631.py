x = int(input())
arr=[]
for _ in range(x):
    arr.append(int(input()))
# arr = list(map(int, input().split()))
dp = [1 for i in range(x)]

for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
        #증가하기만 하면 일단 갱신시켜본다.
            dp[i] = max(dp[i], dp[j]+1)

print(x-max(dp))