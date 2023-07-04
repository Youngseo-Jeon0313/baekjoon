while True:
    flag=-1
    List=list(map(int,input().split()))
    if len(List)==1 and List[0]==0: break
    for i in range(len(List)):
        if i==0: continue
        a=List[i]
        if flag!=a:
            flag=a
            print(a,end=' ')
        if i==len(List)-1: print('$')
