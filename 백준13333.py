import sys
input=sys.stdin.readline

N=int(input())
List=list(map(int,input().split()))
List.sort()
for j in range(N):
    for i in range(10000):
    
        if List[j]>=i and N-i==j :
            print(i); exit()
print(0)

