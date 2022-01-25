'''
(이게 나오면 (2* 시작 
-뒤에가 )이거면 1+로 가고
-뒤에가 [이거면 3*
-뒤에가 (이거면 2*

)이거 
-뒤에가 아무것도 없으면 +0으로 끝내고
-뒤에 ]이거면 +1)



그냥 (이거랑) [이거] 사용하면 될 듯 그리고 그거 그냥
식으로 나타내보기 여러개!
'''
def is_check(s):
    L=[]
    k=0
    for i in s:
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
        return True
    else:
        print(0)
        return False

a=input()
if is_check(a):
    Stack=[]

    for i in a:
        temp=0
        if i=='(':
            Stack.append('(')
        elif i=='[':
            Stack.append('[')
        elif i==')':
            if Stack[-1]=='(':
                Stack.pop()
                Stack.append(2)
            else:
                while Stack[-1]!='(':
                    temp+=Stack[-1]
                    Stack.pop()
                Stack.pop()
                temp*=2
                Stack.append(temp)
        elif i==']':
            if Stack[-1]=='[':
                Stack.pop()
                Stack.append(3)
            else:
                while Stack[-1]!='[':
                    temp+=Stack[-1]
                    Stack.pop()
                Stack.pop()
                temp*=3
                Stack.append(temp)

    print(sum(Stack))