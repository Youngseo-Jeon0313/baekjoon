#누적합 (이게 어떻게 누적합이지? 고찰!!)
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
h=[*map(int,input().split())]

temp=[0]*(n+2)
for i in range(m):
    a,b,k=map(int,input().split())
    temp[a]+=k #애초에 누적합이기 때문에 처음번째에 k를 더함
    temp[b+1]-=k #누적합이기 때문에 마지막꺼+1에 k를 뺌

psum=[0]*(n+2)
for i in range(1,n+1):
    psum[i]=psum[i-1]+temp[i] 
    #temp를 누적합으로 바꿔주기 위한..!!

ans=[0]*n
for i in range(n):
    ans[i]=psum[i+1]+h[i]
print(*ans)
#think.. 굳이 temp를 써야 하는지?? 