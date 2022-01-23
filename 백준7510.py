t=int(input())

for i in range(t):
    a, b, c=map(int ,input().split())

    L=[a,b,c]
    L.sort()

    if L[2]*L[2]==L[0]**2+L[1]**2:
        print("Scenario #{0}:".format(i+1))
        print('yes')
        print()
    else:
        print("Scenario #{0}:".format(i+1))
        print("no")
        print()