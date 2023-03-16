import sys
input=sys.stdin.readline
from heapq import *


ans=0
N=int(input())
List=list(map(int,input().split()))
real_flag=0
K=int(input())
Max=List[0]
for i in range(N):
    Max=max(Max,List[i])
    if List[i]<Max: K-=(Max-List[i]); List[i]=Max; ans=1; real_flag=1
# print(List)
if K<0: print(0)
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
    if len(hq)==1 and not real_flag:
        ans=K//N
        print(ans)
    elif len(hq)==1 and real_flag:
        print(K//N-1)
    else:
        while len(hq)>1:
            real_flag=1
            # print(hq, K, ans)
            a,b=heappop(hq)
            #버튼을 눌렀다.
            c=a+1; d=0
            if hq:
                c,d=heappop(hq)
            K-=b; 
            if K<0: break;
            ans+=1; a+=1
            while a<c and K>0: 
                K-=b; a+=1; ans+=1
            if K<0: break;
            heappush(hq,[a,b+d])
        # print(hq)
        # print("K",K)
        if 
        ans+=K//N
        print(ans)