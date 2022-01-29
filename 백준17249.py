s=input()
flag=True
left=0
right=0
for i in s:
    if i=='(':
        flag=False
    if flag==True:
        if i=='@':
            left+=1
    if flag==False:
        if i=='@':
            right+=1
print(left, right)