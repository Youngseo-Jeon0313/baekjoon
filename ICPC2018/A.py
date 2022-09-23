N=int(input())

for i in range(10000000):
    if i+(i+1)*(2**(i+1)-1)<N<=i+1+(i+2)*(2**(i+2)-1):
        print(i+1); break;
