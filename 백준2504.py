
L=[]
k=0
a=input()


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
            
#일단 되는지 안되는지부터 check

if k==0 and len(L)==0 :
    print(sum)
else:
    print(0)