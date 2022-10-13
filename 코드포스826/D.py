#bfs 느낌
import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    n=int(input())
    List=list(map(int,input().split()))
    LEN=n
    if LEN==1: print(0); continue
    if LEN%2==1: print(-1); continue
    turn=1
    ans=0
    flag=True
    temp=List.copy()
    while LEN>=2:
        TEMP=temp.copy()
        temp=[0 for _ in range(LEN//2)]
        #두개씩 정리
        for i in range(LEN//2):
            if abs(TEMP[2*i]-TEMP[2*i+1])!=1: flag=False; break
            if TEMP[2*i]>TEMP[2*i+1]: ans+=1;
            temp[i]=max(TEMP[2*i+1],TEMP[2*i])//2
        LEN//=2
        
        
    if flag==False: print(-1);
    else: print(ans)
    