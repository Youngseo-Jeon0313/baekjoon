#0 모든 짝수 요소에 더한다.
#1 모든 홀수 요소에 더한다.

t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    List=list(map(int,input().split()))
    SUM=sum(List)
    EVEN=0
    ODD=0
    for i in range(x):
        if List[i]%2: ODD+=1
        else: EVEN+=1
    for _ in range(y):
        type, add=map(int,input().split())
        mul=0
        if type==1:
            print(SUM+ODD*add)
            SUM=SUM+ODD*add
            if add%2==1:
                EVEN+=ODD
                ODD=0
            
        else:
            print(SUM+EVEN*add)
            SUM=SUM+EVEN*add
            if add%2==1:
                ODD+=EVEN
                EVEN=0
            
