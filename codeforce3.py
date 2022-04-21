import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    a=arr[0]%2 #0이라면 짝수
    b=arr[1]%2 
    flag=True
    if a==b: #같다면 계속 같아야 함
        for i in range(2,n):
            if arr[i]%2!=a: flag=False;
    else:
        for i in range(2,n): #홀수번째는 a랑 같고 
            if i%2==0 and arr[i]%2==a : continue
            elif i%2==1 and arr[i]%2==b: continue
            else: flag=False;
        

    if flag==True: print('YES')
    else: print('NO')