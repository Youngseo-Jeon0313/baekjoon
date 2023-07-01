T=int(input())
for _ in range(T):
    N,C=map(int,input().split())
    print(N//C+bool(N%C))