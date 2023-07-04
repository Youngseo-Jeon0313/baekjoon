flag=0
A,B,C,N=map(int,input().split())
for i in range(100):
    for j in range(100):
        for k in range(100):
            if A*i+B*j+C*k==N:
                flag=1
if flag: print(1)
else: print(0)