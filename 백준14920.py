N=int(input())
ans=0
while True:
    if N==1: break
    elif N%2==0: N=N//2
    else: N=3*N+1
    ans+=1
print(ans+1)