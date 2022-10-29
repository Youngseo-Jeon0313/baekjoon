
#최대 공약수
import math

#최소 공배수
def lcm(a,b):
    return a*b//math.gcd(a,b)


a,b=map(int,input().split())
a,b=a//math.gcd(a,b),b//math.gcd(a,b);
sum=0
if a==1: sum+=1;
else:
    while a!=0:
        sum+=1
        x=b//a+bool(b%a)
        b=int(b); x=int(x)
        boonmo=lcm(b,x)
        # print(x,boonmo)
        if ((a*boonmo/b)-(boonmo/x))==0: break;
        else:a=((a*boonmo/b)-(boonmo/x)); b=boonmo;
print(sum)


'''
zerodivisionerror
100
5 86


'''