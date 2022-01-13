N=list(map(int, input().split()))

if ((N[1]//N[3])*(N[2]//N[3])<N[0]):
    print((N[1]//N[3])*(N[2]//N[3]))
else:
    print(N[0])