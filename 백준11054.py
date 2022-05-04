#저 앞쪽부터 한 번 하고
#저 뒷쪽에서부터 한 번 한 다음에 더하기
import sys
input=sys.stdin.readline
x = int(input())
arr = list(map(int, input().split()))
dp_left = [1 for i in range(x)]
dp_right = [1 for i in range(x)]
dp = [1 for i in range(x)]
for i in range(x):
       for j in range(i):
              if arr[i] > arr[j]: dp_left[i] = max(dp_left[i], dp_left[j]+1) 
for i in range(x-1,-1,-1):
       for j in range(x-1,i,-1):
              if arr[i] > arr[j]: dp_right[i] = max(dp_right[i], dp_right[j]+1) 

for i in range(x):
       dp[i]=dp_left[i]+dp_right[i]

print(max(dp)-1)