ans=0
while True:
    operator=''
    a=input()
    if a=='=': print(ans); break
    elif a=='+': operator='+'
    elif a=='*': operator='*'
    elif a=='/': operator='/'
    elif a=='-': operator='-'
    else: 
        a=int(a)
        if operator=='': ans=a
        elif operator=='+': ans+=a
        elif operator=='-': ans-=a
        elif operator=='*': ans+=a
        else: ans/=a
    print('답',ans)