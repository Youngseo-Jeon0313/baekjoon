N=int(input())
arr=list(input())
q=[] #꺼낼 list
value=[] #숫자를 넣을 list
Ans=0
ans=0
for i in range(len(arr)):
    if arr[i] != '*' and arr[i]!='+' and arr[i]!='/' and arr[i]!='-' :
        if ord(arr[i])-64 >len(value):
            value.append(int(input()))
        q.append(value[ord(arr[i])-65])
    else:
        a=q.pop();b=q.pop()
        if arr[i]=='+':q.append(a+b)
        elif arr[i]=='*': q.append(a*b)
        elif arr[i]=='-': q.append(b-a)
        elif arr[i]=='/': q.append(b/a)
print('{:.2f}'.format(q[0]))