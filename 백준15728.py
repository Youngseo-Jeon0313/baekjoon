import sys
input=sys.stdin.readline

N,K=map(int,input().split())
share= list(map(int,input().split()))
team=list(map(int,input().split()))

List=[[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        List[i][j]=team[i]*share[j] #기준 Team
List_=[0 for _ in range(N)]
for i in range(N):
    List_[i]=max(List[i])

List_.sort(reverse=True)
# print(List_)
print(List_[K])