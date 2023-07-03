T=int(input())
for _ in range(T):
    n=int(input())
    List=list(map(int,input().split()))
    print(min(List), max(List))