t=int(input())
for _ in range(t):
    x,y,a,b=map(int,input().split())
    if x*y<a*b: print("Eurecom")
    elif x*y>a*b: print("TelecomParisTech")
    else: print("Tie")