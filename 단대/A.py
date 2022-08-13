import sys 
input=sys.stdin.readline

N,M,a,K=map(int,input().split())
#사람들 1사람씩
if (a-K)//(N-1)>0: print(N , end=" ")
else: print(a-K+1, end=" ")
#꽉찬다고 하면
print((a-K)//M+bool((a-K)%M)+1)

