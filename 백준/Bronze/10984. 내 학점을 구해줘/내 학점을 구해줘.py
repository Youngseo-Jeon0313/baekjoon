t=int(input())
for _ in range(t):
    n=int(input())
    Sum=0; sum=0
    for _ in range(n):
        a,b=input().split()
        a=int(a); b=float(b)
        Sum+=a*b
        sum+=a
    print(sum,round(Sum/sum,1))