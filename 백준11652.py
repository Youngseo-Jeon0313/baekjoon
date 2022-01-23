N=int(input())


D={}
for i in range(N):
    a=input()
    if a in D.keys():
        D[a] +=1
    else:
        D[a]=1

L=list(D.values())
L.sort(reverse=True)
MAX=L[0]

K=[]
for key, value in D.items():
    if value ==MAX:
        K.append(int(key))
K.sort()
print(K[0])
