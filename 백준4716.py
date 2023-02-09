import sys
input=sys.stdin.readline

while True:
    n,a,b=map(int,input().split())
    if n==0 and a==0 and b==0: break
    arr=[list(map(int,input().split())) for _ in range(n)]
    arr=sorted(arr,key=lambda x:[abs(x[1]-x[2]),x[1]], reverse=True)
    ans=0
    equal_dis=[]
    for ballon, distanceA, distanceB in arr:
        if distanceA > distanceB:
            if b >= ballon:
                b -= ballon
                ans += distanceB * ballon
            else:
                ballon -= b
                ans += distanceB * b
                b = 0
                ans += distanceA * ballon
        else:
            if a >= ballon:
                a -= ballon
                ans += distanceA * ballon
            else:
                ballon -= a
                ans += distanceA * a
                a = 0
                ans += distanceB * ballon
    print(ans)