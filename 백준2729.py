t=int(input())

for i in range(t):
    a,b=input().split()
    a=list(a)
    b=list(b)
    a=a[::-1]
    b=b[::-1]
    La=len(a)
    Lb=len(b)
    L=max(La,Lb)
    if L==Lb:
        for i in range(Lb-La):
            a.append(0)
    else:
        for i in range(La-Lb):
            b.append(0)
    a.append(0)
    b.append(0)
    answer=[]
    for i in range(L+1):
        answer.append(0)
    for i in range(L+1):
        if int(a[i])+int(b[i])==1:
            answer[i]=1
        elif int(a[i])+int(b[i])==0:
            answer[i]=0
        elif int(a[i])+int(b[i])==2:
            answer[i]=0
            a[i+1]=int(a[i+1])+1
            
        elif int(a[i])+int(b[i])==3:
            answer[i]=1
            a[i+1]=int(a[i+1])+1
            
    answer=answer[::-1]
    flag=True
    for i in answer:
        if i==0:
            if flag==False:
                print(i,end='')
        else:
            flag=False
            print(i,end='')
    if flag==True:
        print(0,end='')
    print()
