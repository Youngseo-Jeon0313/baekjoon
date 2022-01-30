a,b=map(int, input().split())

picture=[]
for i in range(a):
    s1=input()
    picture.append(s1)

picture_2=[]
for i in range(a):
    s2=input()
    picture_2.append(s2)

flag=True
for i in range(a):
    for j in range(b):
        if picture[i][j]!=picture_2[i][2*j]:
            flag=False
            break
        if picture[i][j]!=picture_2[i][2*j+1]:
            flag=False
            break
if flag==True:
    print('Eyfa')
else:
    print('Not Eyfa')
