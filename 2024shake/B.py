N, K =map(int,input().split())
gong = 1
for i in range(K-1,0,-1):
    if N%i==0:
        gong=i
if N%K==0: print(0)
else:
    print((N//gong)*(K//gong-1))