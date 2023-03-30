N=int(input())
for i in range(2,5000000):
    if (i-1)*(i-2)//2 < N <=i*(i-1)//2:
        if (i%2):
            print(N-(i-1)*(i-2)//2,'/', i-(N-(i-1)*(i-2)//2),sep='')
        else:
            print( i-(N-(i-1)*(i-2)//2),'/',N-(i-1)*(i-2)//2,sep='')