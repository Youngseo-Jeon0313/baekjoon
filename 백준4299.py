'''
a+b=N
a-b=M
a=(N+M)//2
b=(N-M)//2
'''
N,M=map(int,input().split())
a=(N+M)//2
b=(N-M)//2
if a<b: a,b=b,a
print(a,b)