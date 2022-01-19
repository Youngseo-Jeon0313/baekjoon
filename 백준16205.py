a,b=input().split()
a=int(a)
if a==1: #카멜 표기법
    print(b)
    for i in range(len(b)): 
        if b[i].isupper():
            print('_',end='')
            print(b[i].lower(),end='')
            continue  
        print(b[i],end='')
    print()      
    print(b[0].capitalize(),end='')
    print(b[1:])
elif a==2: #스네이크 표기법
    if '_' in b:
        c,d=b.split('_')
        print(c,d.capitalize(),sep='')
        print(b)
        print(c.capitalize(),d.capitalize(),sep='')
    else:
        print(b)
        print(b)
        print(b.capitalize())
elif a==3: #파스칼 표기법
    print(chr(ord(b[0])+32),end='')
    print(b[1:])
    print(chr(ord(b[0])+32),end='')
    for i in range(1,len(b)): 
        if b[i].isupper():
            print('_',end='')
            print(b[i].lower(),end='')
            continue  
        print(b[i],end='')
    print()
    print(b)