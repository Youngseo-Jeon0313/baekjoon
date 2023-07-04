N=int(input())
for _ in range(N):
    List=list(input().split())
    a,b=0,0
    for i in List:
        for j in i:
            if j in ['A','E','O','U','I','a','e','o','i','u']:
                a+=1
            else: b+=1
    print(b,a)