N,M=map(int,input().split())
A=list(input())
B=list(input())
T=int(input())

start=A[::-1]+B
for _ in range(T):
    flag=False; #바뀜을 확인하는 flag
    for i in range(N+M-1):
        if start[i] in A and start[i+1] in B:
            start[i],start[i+1]=start[i+1],start[i]; 
        # print(start)
            if start[i+1]==A[0]: break
print(*start,sep='')