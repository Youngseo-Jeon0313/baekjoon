import sys
input=sys.stdin.readline

N,X=map(int,input().split())
if N*26<X or N>X: print("!")
else:
    List=['A' for _ in range(N)]
    X-=N
    for i in range(N-1,-1,-1):
        if X>25: 
            List[i]='Z'
            X-=25
        else:
            List[i]=chr(ord('A')+X)
            break
    print("".join(List))