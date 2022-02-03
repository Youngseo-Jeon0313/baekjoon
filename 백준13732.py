import sys
sys.setrecursionlimit(100000)

N,M=map(int, sys.stdin.readline().split())
arr=[]
for i in range(N):
    arr.append(list(input()))


for j in range(M):
    a=0; b=0
    for i in range(N):
        if arr[i][j]=='a':
            a+=1
        elif arr[i][j]=='.':
            b+=1
        if arr[i][j]=='#':
            for k in range(i+1):
                if b>0:
                    arr[k][j]='.'
                    b-=1
                elif a>0:
                    arr[k][j]='a'
                    a-=1
            break
        elif i==N-1:
            for k in range(i+1):
                if b>0:
                    arr[k][j]='.'
                    b-=1
                elif a>0:
                    arr[k][j]='a'
                    a-=1
            break

for i in range(N):
        print(''.join(arr[i]))
