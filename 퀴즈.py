import sys
input=sys.stdin.readline

N,Q=map(int,input().split())
arr=list(map(int,input().split()))
ans=0
arr_zero=[0 for _ in range(N+1)]
arr_zero[0]=arr[0]
for i in range(N):
    arr_zero[i+1]=arr_zero[i]^arr[i]
# print(arr_zero)
for i in range(Q):
    a,b=map(int,input().split())
    ans^=arr_zero[a-1]^arr_zero[b]
    # print('ans:',ans)
print(ans)

