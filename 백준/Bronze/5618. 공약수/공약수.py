import math

def lcm(a,b):
    return int((a*b)/gcd(a,b))

def gcd(a,b):
    if a==0: return b
    else:
        return gcd(b%a,a)

N=int(input())
List=list(map(int,input().split()))
if len(List)==2:
    ans=(gcd(List[0],List[1]))
else:
    temp=gcd(List[0],List[1])
    ans=(gcd(temp,List[2]))
lst=[]
for i in range(1, int(math.sqrt(ans)) + 1):
    if ans % i == 0:
        lst.append(i)
        if i**2 != ans:
            lst.append(ans // i)
lst=sorted(lst)
for i in lst:
    print(i)