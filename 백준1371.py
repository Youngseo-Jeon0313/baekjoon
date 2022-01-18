import sys
L=''
for line in sys.stdin:
    L+=line
    
L=list(L.split())

D={}
for i in L:
    for j in range(len(i)):
        if i[j] in list(D.keys()): 
            D[i[j]]+=1
        else:
            D[i[j]]=1

Check=list(D.values())
Check.sort(reverse=True)

if len(Check)==1:
    print(L[0][0])
elif Check[0]!=Check[1]:
    Max=Check[0]
    for key, value in D.items():
        if value == Max:
            print(key)
else:
    Max=Check[0]
    E=list()
    for key,value in D.items():
        if value == Max:
            E.append(key)
    E.sort()
    for i in E:
        print(i,end='')