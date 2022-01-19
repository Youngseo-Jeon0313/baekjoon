L=int(input())
t=int(input())


Max=0
Max_id=0
LIST=[0 for j in range(L)]
for i in range(1,t+1):
    P,K=input().split()
    P=int(P)
    K=int(K)
    if K-P>Max:
        Max=K-P
        Max_id=i
    for k in range(P-1,K):
        if LIST[k]==0:
            LIST[k]=i
        else:
            continue
print(Max_id)

D={}
for j in LIST:
    if j in D.keys():
        D[j]+=1
    else:
        D[j]=1
if 0 in D:
    D.pop(0)


Key=list()
for key, value in D.items():
    P=list(D.values())
    P.sort()
    if value==P[-1]:
        Key.append(key)

print(Key[0])



#입력받는 수는 리스트에 있는 거랑 다른 거 인지!1!!