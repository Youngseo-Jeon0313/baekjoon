T=int(input())
#최대 공약수
import math

#최소 공배수
def lcm(a,b):
    return a*b//math.gcd(a,b)

for _ in range(T):
    a,b=map(int,input().split())
    print(math.gcd(a,b))
    a,b=a//math.gcd(a,b),b//math.gcd(a,b);
    if a==1: print(int(b));
    else:
        while True:
            print(a,b)
            x=b//a+bool(b%a)
            b=int(b); x=int(x)
            boonmo=lcm(b,x)
            # print(x,boonmo)
            if ((a*boonmo/b)-(boonmo/x))==1:print(int(boonmo)); break;
            else:a=((a*boonmo/b)-(boonmo/x)); b=boonmo;
    

'''
zerodivisionerror
100
5 86


'''