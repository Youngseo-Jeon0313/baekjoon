ans=0
giho='+'
while True:
    a=input()
    if a=='=': break
    if a not in ['+','-','*','/']:
        ans=str(int(eval(str(ans)+giho+a)))
    else:
        giho=a
print(ans)