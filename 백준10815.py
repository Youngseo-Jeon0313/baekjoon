N=int(input())
Sang=list(map(int,input().split()))

M=int(input())
Card=list(map(int,input().split()))

for i in Card:
    if i in Sang: print(1,end=' ')
    else: print(0, end=' ')