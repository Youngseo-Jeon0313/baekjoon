N=int(input())
a=''
while True:
    if N==0:
        break
    a+=str(N%2)
    N//=2

print(int(a,2))
