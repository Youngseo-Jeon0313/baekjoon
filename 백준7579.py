import sys
input=sys.stdin.readline

N,M=map(int,input().split()) #M바이트를 확보하기 위해!!
'''
M바이트가 넘는 이슈??
그건 그냥 M바이트 넘을 때 M에다가 등록해주면 될 것 같다.
'''

'''
시간초과를 타겟팅한 문제..
메모리바이트를 하지 말고 비용으로 ㄱㄱㄱ
'''
Memory=list(map(int,input().split()))
Cost=list(map(int,input().split()))
DP=[-1 for _ in range(100*100+1)] #N*max(CN)  해당 비용이라면 얼마만큼의 메모리를 확보할 수 있는가 ?
#DP[해당비용에서의] = 최대의 메모리
DP[0]=0


for i in range(N): #입력받은 것들을 순서대로 돌 것이다.
    for j in range(10000,-1,-1):
        if DP[j]!=-1:
            DP[j+Cost[i]]=max(DP[j+Cost[i]],DP[j]+Memory[i])
ans=10000

for i in range(10000):
    if DP[i]>=M:
        ans=min(ans,i)
print(ans)