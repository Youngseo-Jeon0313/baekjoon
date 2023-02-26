import sys
input=sys.stdin.readline

List=[]
temp=0
for i in range(10000000):
    List.append(temp+i)
    temp=temp+i

N=int(input())
if N==1: print(1)
else:
    for i in range(1,10000000):
        if 6*List[i]+2>N and 6*List[i-1]+1<N: print(i+1); break;
