N=int(input())
while True:
    a=int(input())
    if a==0: break;
    if a%N: print("{} is NOT a multiple of {}.".format(a,N))
    else: print("{} is a multiple of {}.".format(a,N))