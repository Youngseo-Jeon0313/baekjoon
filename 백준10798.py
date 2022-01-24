L=[]

for i in range(5):
    L.append(list(input()))
    for j in range(len(L[i])+1,16):
        L[i].append(-1)

for i in range(15):
    for j in range(5):
        if L[j][i]==-1:
            continue
        else:
            print(L[j][i], end='')