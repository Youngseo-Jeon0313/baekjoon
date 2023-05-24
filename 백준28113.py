N,A,B=map(int,input().split())
if A==B and N<=B: print('Anything')
elif A<B or N>B: print("Bus")
else: print("Subway")