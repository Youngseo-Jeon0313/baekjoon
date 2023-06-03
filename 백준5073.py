while True:
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0: break
    L=[a,b,c]
    L=sorted(L)
    # print(L)
    if L[2]>=L[1]+L[0]: print("Invalid")
    elif len(set(L))==1: print("Equilateral")
    elif len(set(L))==2: print("Isosceles")
    else: print("Scalene")