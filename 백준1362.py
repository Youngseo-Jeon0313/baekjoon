'''
너무 EOF 에 집착하지 말고 while True 문으로 계속 입력받는 것도 좋다!

'''
i=0
while True:
    a,b = input().split() #적정체중/실제체중 입력받고
    if a=='0' and b=='0':
        exit()
    i+=1
    a=int(a)
    b=int(b)
    die=False
    while True:
        c,d=input().split()
        if c=='#' and d=='0':
            break
        
            
        if c=='F':
            b+=int(d)
        else:
            b-=int(d)
            if b<=0:
                die=True
    if die==True:
       print(i,'RIP')
    elif a/2<b and b<2*a:
        print(i,':-)')
    else:
        print(i,":-(") 


'''

break문을 웨에서 썼는데 뒤에서
그 전에 받은 변수 쓰면 런타임에러
'''