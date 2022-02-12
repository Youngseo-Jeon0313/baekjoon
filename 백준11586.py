N=int(input())
arr=list(list(input()) for _ in range(N))
state=int(input())

if state==1:
    for i in range(N):
        print(''.join(arr[i]))
elif state==3:
    for i in range(N-1,-1,-1):
        print(''.join(arr[i]))
else:
    for i in range(N):
        for j in range(N-1,-1,-1):
            print(arr[i][j],end='')
        print()
