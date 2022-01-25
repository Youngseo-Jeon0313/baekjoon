from collections import deque
import sys
input=sys.stdin.readline

t=int(input())
for i in range(t):
    N,M=map(int, input().split())
    Remove=0
    List=deque(map(int,input().split()))
    if N==1:
        print(1)
    else:
        while True:
            if M==-1:
                break
            if List[0]!=max(List): #더 큰게 하나라도 있으면
                    x=List.popleft()
                    List.append(x)
                    if M==0:
                        M+=(N-1)
                    else:
                        M-=1
            else:
                List.popleft()
                Remove+=1
                M-=1
                N-=1
                continue
            
        print(Remove)