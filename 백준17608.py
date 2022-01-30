N=int(input())
Box=[]
for i in range(N):
    s=int(input())
    if len(Box)>0:
        for j in range(len(Box)):
            if int(Box[j])<=s:
                Box.pop(j)
    Box.append(s)
print(Box)