A=list(map(int, input().split()))
B=list(map(int, input().split()))
C=[0,0,0,0,0,0,0,0,0,0]
a=0
b=0
check=0

for i in range(10):
    if A[i] > B[i]:
        a+= 3
    elif A[i] < B[i]:
        b+=3
    else:
        a+=1
        b+=1

print(a,b)
if a>b:
    print('A')
elif a<b:
    print('B')
else:
    for i in range(10):
        if A[i]<B[i] :
            C[i] ='B'
        elif A[i] >B[i] :
            C[i] ='A'
        else :
            C[i] = 'D'
    for i in range(9,-1,-1):
        if C[i]=='A' :
            print('A')
            check+=1
            break
        elif C[i]=='B':
            print('B')
            check+=1
            break
    if check==0:
        print('D')
