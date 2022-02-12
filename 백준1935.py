N=int(input())
arr=list(input())
q=[];value=[]
flag=False
Ans=0
ans=0
for i in range(len(arr)):
    if arr[i] != '*' and arr[i]!='+' and arr[i]!='/' and arr[i]!='-' :
        if ord(arr[i])-64 >len(value):
            value.append(int(input()))
        q.append(value[ord(arr[i])-65])
        Ans=ans
        ans=0
        flag=False
    else:
        if flag==False: ans=q.pop(); flag=True
        
        if arr[i]=='+': ans+=q.pop()
        elif arr[i]=='*': ans*=q.pop()
        elif arr[i]=='-': ans=q.pop()-ans
        elif arr[i]=='/': ans=q.pop()/ans
        if q==[]:
            if arr[i]=='+': Ans+=ans
            elif arr[i]=='-': Ans-=ans
            elif arr[i]=='*': Ans+=ans
            else: Ans/=ans
    print(q, Ans, ans)
print('{:.2f}'.format(Ans))