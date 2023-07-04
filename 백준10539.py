N=int(input())
List=list(map(int,input().split()))
for i in range(N):
    List[i]*=(i+1)
for i in range(N):
    if i==0: print(List[i], end=' ')
    else: print(List[i]-List[i-1], end=' ')