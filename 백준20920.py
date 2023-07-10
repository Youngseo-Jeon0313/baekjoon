import sys

N,M=map(int,input().split())
List=[]
for _ in range(N):
    List.append(sys.stdin.readline().rstrip())
List=sorted(List, key =lambda x : [-List.count(x), -len(x), x])
List=set(List)
List=list(List)
print(List)
print('-------------')
for i in range(len(List)):
    if len(List[i])>=M:
        print(List[i])