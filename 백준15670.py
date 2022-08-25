import sys
input=sys.stdin.readline

N,M=map(int,input().split())
List=list(map(int,input().split()))
#전처리

incline_prefix=[0 for _ in range(N)]
incline_prefix[0]=1
for i in range(1,N):
    if List[i-1]>List[i]: incline_prefix[i]=incline_prefix[i-1]+1
    else: incline_prefix[i]=incline_prefix[i-1]
decline_prefix=[0 for _ in range(N)]
decline_prefix[0]=1
for i in range(1,N):
    if List[i-1]<List[i]: decline_prefix[i]=decline_prefix[i-1]+1
    else: decline_prefix[i]=decline_prefix[i-1]

# print(incline_prefix)
# print(decline_prefix)
for _ in range(M):
    x,y=map(int,input().split())
    x=x-1; y=y-1
    diff=decline_prefix[y]-decline_prefix[x]+1
    #구간 1 2 3으로 나누어서 생각
    #1과 2가 겹칠수 있는지
    if x>0:
        diff+=incline_prefix[x-1]
        if List[y]>List[x-1]: diff-=1
    
    #2와 3이 겹칠 수 있는지
    if y<N-1:
        diff+=(incline_prefix[N-1]-incline_prefix[y+1]+1)
        if List[y+1]>List[x]: diff-=1
    print(diff)

