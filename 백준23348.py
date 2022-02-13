A,B,C=map(int, input().split())
Dong=int(input())
MAX=0
for i in range(Dong):
    sum=0
    for j in range(3):
        a,b,c=map(int,input().split())
        sum+=a*A + b*B + c*C
    if sum>MAX: MAX=sum
print(MAX)