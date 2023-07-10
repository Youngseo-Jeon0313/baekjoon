N,M=map(int,input().split())
A=list(input())
B=list(input())
T=int(input())

start=A[::-1]+B
for _ in range(T):
    flag=False; #바뀜을 확인하는 flag
    for i in range(1,N+M):
        if start[i-1] in A and start[i] in B:
            start[i],start[i-1]=start[i-1],start[i]; 
        # print(start)
print(*start,sep='')