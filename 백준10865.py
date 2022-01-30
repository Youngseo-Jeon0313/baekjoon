import sys
input=sys.stdin.readline

N, M=map(int, input().split())

D={}

for i in range(M):
    student1, student2=map(int,input().split())
    if student1 in D.keys():
        D[student1]+=1
    else:
        D[student1]=1
    if student2 in D.keys():
        D[student2]+=1
    else:
        D[student2]=1

for i in range(1,N+1):
    if i not in D.keys():
        D[i]=0

for key, value in sorted(D.items()):
    print(value)