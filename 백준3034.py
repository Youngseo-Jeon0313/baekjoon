N,W,H=map(int,input().split())
for _ in range(N):
    a=int(input())
    if a**2<=W**2+H**2: print("DA")
    else: print("NE")