#스택의 위엄을 알려주는 문제
#K개를 "지웠을 때!!"

import sys
input=sys.stdin.readline


N,K=map(int,input().split())

num_list=list(input())
stack=[]
for i in range(N):
    while stack and stack[-1]<num_list[i] and K>0:
        # print(K)
        stack.pop()
        K-=1
    stack.append(num_list[i])
    # print(stack)
if K>0:
    print(''.join(stack[:-K]))
else:
    print(''.join(stack))