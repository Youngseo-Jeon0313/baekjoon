import sys
input=sys.stdin.readline

for _ in range(3):
    N=int(input())
    SUM=0   
    for _ in range(N):
        SUM+=int(input())
    if SUM==0: print("0")
    elif SUM>0: print("+")
    else: print("-")