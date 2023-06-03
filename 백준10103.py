N=int(input())
A=100; B=100;
for _ in range(N):
    a,b=map(int,input().split())
    if a<b: A-=b
    elif a>b: B-=a

print(A)
print(B)