N=int(input())
a,b,c,d,e=map(int,input().split())

sum = 0
if a==N:
    sum+=1
if b==N:
    sum+=1
if c==N:
    sum+=1
if d==N:
    sum+=1
if e==N:
    sum+=1

print(sum)