import sys
input=sys.stdin.readline

N=int(input())
List=[]
for i in range(N):
    x,y=map(int,input().split())
    List.append([x,y])
List=sorted(List, key = lambda x:[x[0],x[1]])
for i in List:
    print(i[0], i[1])