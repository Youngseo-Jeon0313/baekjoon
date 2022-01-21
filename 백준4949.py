while True:
    L=[]
    k=0
    a=input()
    if a=='.':
        break

    for i in a:
        if i=='(' or i=='[':
            L.append(i)
        elif i==')':
            if len(L)==0 or L[-1]=='[':
                k=1
                break
            elif L[-1]=='(':
                L.pop()     
     
        elif i==']':
            if len(L)==0 or L[-1]=='(':
                k=1
 
                break
            elif L[-1]=='[':
                L.pop()
                


    if k==0 and len(L)==0 :
        print('yes')
    else:
        print('no')