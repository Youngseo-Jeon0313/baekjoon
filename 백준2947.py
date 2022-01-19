A,B,C,D,E=input().split()
A=int(A)
B=int(B)
C=int(C)
D=int(D)
E=int(E)

T=0
while True:
    if A>B:
        T=A
        A=B
        B=T
        print(A,B,C,D,E)
    if B>C: 
        T=B
        B=C
        C=T
        print(A,B,C,D,E)
    if C>D: 
        T=C
        C=D
        D=T
        print(A,B,C,D,E)
    if D>E: 
        T=D
        D=E
        E=T
        print(A,B,C,D,E)
    if (A==1 and B==2 and C==3 and D==4 and E==5):
        break
    else:
        continue
