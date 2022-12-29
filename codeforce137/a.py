import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    D=dict()
    for i in range(10):
        D[i]=0
    n=int(input())
    List=list(map(int,input().split()))
    for i in range(n):
        D[List[i]]=1
    ans=0
    for key, value in D.items():
        if D[key]==0:
            ans+=1
    print(6*ans*(ans-1)//2)   