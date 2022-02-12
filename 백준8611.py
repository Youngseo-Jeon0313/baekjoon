number=int(input())
flag=True
for i in range(2,11):
    n=number
    tmp=''
    while n:
        tmp+=str(n%i)
        n//=i
    if tmp==tmp[::-1]:
        print(i, tmp)
        flag=False
if flag==True:
    print('NIE')