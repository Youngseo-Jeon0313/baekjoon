'''
예제: A*B-C*D/E -> AB*CD*E/-
'''


s=input()
Alpha=[]; Giho=[]; 
for i in range(len(s)):
    if s[i]=='(': Giho.append('(')
    elif s[i]==')':  
        print(*Alpha,sep='',end=''); Alpha=[];
        while True:
            if len(Giho)==0: break
            if Giho[-1]=='(': Giho.pop(); break;
            x=Giho.pop(); 
            print(x,sep='',end='')
    else: 
        if i==(len(s)-1): Alpha.append(s[i]); print(*Alpha,sep='',end=''); print(*Giho[::-1],sep='',end='');Giho=[]
        elif s[i]=='*' or s[i]=='/': 
            if len(Giho)>0 and (Giho[-1]=='*' or Giho[-1]=='/'):
                print(*Alpha,sep='',end=''); Alpha=[];
                while True:
                    if len(Giho)==0 or (Giho[-1]=='+' or Giho[-1]=='-'): break
                    if Giho[-1]=='(':break;
                    x=Giho.pop(); 
                    print(x,sep='',end='')
            Giho.append(s[i])
        elif s[i]=='+' or s[i]=='-':
            if len(Giho)>0 and (Giho[-1]=='*' or Giho[-1]=='/'):
                print(*Alpha,sep='',end=''); Alpha=[]
                while True:
                    if len(Giho)==0: break
                    if Giho[-1]=='(':break;
                    x=Giho.pop(); 
                    print(x,sep='',end='')
            elif len(Giho)>0 and (Giho[-1]=='+' or Giho[-1]=='-'):
                print(*Alpha,sep='',end=''); Alpha=[]
                while True:
                    if len(Giho)==0 : break
                    if Giho[-1]=='(': break;
                    x=Giho.pop(); 
                    print(x,sep='',end='')
            Giho.append(s[i])
        else: Alpha.append(s[i])
if len(Giho)>0: print(*Giho[::-1],sep='')