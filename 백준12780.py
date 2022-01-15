H=input()
N=input()
sum =0

for i in range(len(H)-len(N)+1):
    if H[i:i+len(N)] ==N:
        sum+=1

print(sum)






