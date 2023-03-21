import sys
input=sys.stdin.readline

n=int(input())
Num=[0 for _ in range(51)]
List=list(map(int,input().split()))

for i in List:
    Num[i]+=1

flag=False
for j in range(50,-1,-1):
    if Num[j]==j:
        print(j); flag=True; break;

if not flag: print(-1)