import sys
input = sys.stdin.readline
k = int(input())
n,cnt= 1,0
while(n<k):
    n*=2
if n==k:
    print(n, 0)
else:
    ans = n
    # k에서 역으로 계산
    while(k>0):
        if k>=n:
            k-=n
        else:
            n//=2
            cnt+=1
    print(ans, cnt)