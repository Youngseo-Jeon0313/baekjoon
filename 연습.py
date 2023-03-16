import sys
input=sys.stdin.readline
from heapq import *


ans=0
N=int(input())
List=list(map(int,input().split()))
K=int(input())
Max=List[0]
for i in range(N):
    Max=max(Max,List[i])
    if List[i]<Max: K-=(Max-List[i]); List[i]=Max; 

if K<0: print(ans)
else:
    ans=1
    hq=[]
    flag=List[0]; num=0
    List+=[-1]
    for i in List:
        if flag==i: num+=1
        else: 
            heappush(hq,[flag,num])
            num=1; flag=i; 
    # print(hq)
    while True:
        a,b=heappop(hq)
        #버튼을 눌렀다.
        c=a+1; d=0
        if hq:
            c,d=heappop(hq)
        K-=b; 
        if K<=0: break;
        ans+=1; a+=1
        while a<c and K>0:
            K-=b; a+=1; ans+=1
        if K<=0: break;
        heappush(hq,[a,b+d])
        if K<0: ans-=1
        if K>0:
            ans+=K//N
    print(ans)