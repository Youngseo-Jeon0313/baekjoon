a,b=input().split()

if a=='1': #카멜 표기법
    print(b)
    for i in range(len(b)): 
        if b[i].isupper():
            print('_',end='')
            print(chr(ord(b[i])+32),end='') # 소문자 출력
        else: print(b[i],end='')
    print()
    print(chr(ord(b[0])-32),end='') #맨 앞글자만 대문자로 바꾸기
    print(b[1:])
elif a=='2': #스네이크 표기법
    #_가 나올때마다 그거 지워주고 바로 다음 글자를 대문자로
    i=0
    while i <len(b):
        if b[i]=='_':
            i+=1
            print(chr(ord(b[i])-32),end='')
            i+=1
            continue
        print(b[i],end='')
        i+=1
    print()
    print(b)
    print(chr(ord(b[0])-32),end='')
    i=1
    while i <len(b):
        if b[i]=='_':
            i+=1
            print(chr(ord(b[i])-32),end='')
            i+=1
            continue
        print(b[i],end='')
        i+=1
    print()
    
elif a=='3': #파스칼 표기법
    print(chr(ord(b[0])+32),end='')
    print(b[1:])
    print(chr(ord(b[0])+32),end='')
    for i in range(1,len(b)): 
        if b[i].isupper():
            print('_',end='')
            print(chr(ord(b[i])+32),end='')
            continue  
        print(b[i],end='')
    print()
    print(b)