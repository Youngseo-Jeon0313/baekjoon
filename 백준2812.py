import sys
input=sys.stdin.readline


N,K=map(int,input().split())

num_list=list(input())
stack=[]
for i in range(N):
    while stack and stack[-1]<num_list[i] and K>0:
        stack.pop()
        K-=1
    stack.append(num_list[i])
if K>0:
    print(''.join(stack[:-K]))
else:
    print(''.join(stack))