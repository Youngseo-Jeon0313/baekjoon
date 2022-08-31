N=int(input())
L=list(map(int,input().split()))

if N==1 and max(L)==1: print('Happy')
elif sum(L)-2*max(L)<0: print('Unhappy')
else: print('Happy')