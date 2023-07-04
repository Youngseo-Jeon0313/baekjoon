N=input()
if N[:2]=='0x':
    print(int(N,16))
elif N[0]=='0':
    print(int(N,8))
else: 
    print(int(N))

