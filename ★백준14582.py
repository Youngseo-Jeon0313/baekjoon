'''
입력을 받은 후 
a를 더하고 
판단
b더하고 .
이런식으로 가야 한ㄷㅏ!!



문제를 잘 읽자. 
★경기는 ~~순이다. 이거 말해준 이유가 있다.
★이미 이기는 건 B이다.
'''



U=[]
S=[]
R=[]
sum_A=0
sum_B=0
flag=False
a=list(map(int,input().split()))
b=list(map(int, input().split()))


for i in range(9):
    sum_A+=int(a[i])
    if sum_A>sum_B:flag=True
    sum_B+=int(b[i])
    

if flag==True:
    print("Yes")
else:
    print("No")