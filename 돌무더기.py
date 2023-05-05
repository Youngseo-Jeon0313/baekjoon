def solve(l,n,m,turn):
    if l==0 and n==0 and m==0:
        return turn
    if (l>=1 and solve(l-1, n,m,1-turn)) or (l>=2 and solve(l-2, n,m,1-turn))\
    or (n>=1 and solve(l, n-2,m,1-turn)) or (n>=2 and solve(l, n-2,m,1-turn))\
    or (m>=1 and solve(l, n,m-1,1-turn)) or (l>=2 and solve(l, n,m-2,1-turn)):
        return turn
    else:
        return 1-turn
    
l=1
n=0
m=0
result=solve(l,n,m,0)
if result==0:
    print("A wins")
else:
    print("B wins")    