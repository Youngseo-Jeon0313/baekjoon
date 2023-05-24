'''
규칙이 있다!
엄지 - 1 9 17 ..
검지 - 2 8 10 16 ..
'''



N=int(input())
if N%8==1: print(1)
elif N%8==5: print(5)
elif N%8==0 or N%8==2: print(2)
elif N%8==3 or N%8==7: print(3)
else: print(4)