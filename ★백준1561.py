import sys
input=sys.stdin.readline

N,M=map(int,input().split())
time=list(map(int,input().split()))
#1부터  2000000000*30까지의 운행시간 중에서 마지막 학생이 
#놀이기구에 타게 되는 시간을 구한다.

#init
start=0; end=600000000000;
if N<=M: print(N); exit();

while start<=end: #이분탐색 구간을 나오면 
    ans=M
    mid=(start+end)//2 
    for i in time: 
        ans+=mid//i #나머지 신경 안 써도 됨 -> 걸리는 거 +1 / 애매하게 걸린 거는 포함 
    if ans>=N: 
        MID=mid #왜???????????????????????????????????/
        end=mid-1
    else: 
        start=mid+1 
# print(mid,ans)
ans=M
for j in time: #딱 그 전까지의 학생들이 몇 명 들어오는지 구한다.
    ans+=(MID-1)//j
# print(ans)
for i in range(len(time)):
    if (MID)%time[i]==0: ans+=1
    if ans==N: print(i+1); exit()


'''
이분탐색에서 애매하게 걸리는 애들 + 딱 맞아떨어지는 애들 표현 주의
ans=M
for i in time: 
        ans+=mid//i #나머지 신경 안 써도 됨 -> 걸리는 거 +1 / 애매하게 걸린 거는 포함 
이 부분이랑
for i in range(len(time)):
    if (MID)%time[i]==0: ans+=1 
이부분 에서는 딱맞아떨어지는 애들 제외하고 이제 새롭게 시작하는 애들 더하는 방식

'''
