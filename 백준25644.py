import sys
input=sys.stdin.readline


N=int(input())
List=list(map(int,input().split()))
left=0; right=N-1;
result=-float('inf'); MAX=-float('inf')

for i in range(N-1,-1,-1):
    MAX=max(MAX, List[i])
    result=max(result, MAX-List[i] )

print(result)