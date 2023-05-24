A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())

ans=0
if A<0: 
    ans+=abs(A)*C
    A+=abs(A)
    ans+=D
if A>=0:
    ans+=(B-A)*E
print(ans)