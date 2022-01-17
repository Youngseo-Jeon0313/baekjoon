L=list(input().lower())

D={}
for i in L:
    if i in D.keys():
        D[i]+=1
    else:
        D[i]=1

L=list(D.keys())
V=list(D.values())
V.sort(reverse=True)

if len(L)==1:
    print(L[0].upper())
elif V[0]==V[1]:
    print('?')
else:
    Max=V[0]
    for key, value in D.items():
        if value ==Max:
            print(key.upper())