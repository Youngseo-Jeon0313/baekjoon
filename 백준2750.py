t=int(input())

A=list()

for i in range(t):

    A.append(int(input()))

A.sort()

A=tuple(A)

for i in A:

    print(i)