L=int(input())
A=int(input())
B=int(input())
C=int(input())
D=int(input())
M=max(A//C+bool(A%C),B//D+bool(B%D))
print(L-M)