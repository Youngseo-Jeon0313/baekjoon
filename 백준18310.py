N=int(input())
List=list(map(int,input().split()))
List=sorted(List)
if N%2==0:
    print(List[N//2-1])
else:
    print(List[N//2])