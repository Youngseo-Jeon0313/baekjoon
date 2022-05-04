
stack=[]

A=input()
B=input()
i=0 ; j=0;
flag=False

for i in range(len(A)):
    stack.append(A[i])
    if stack[-1]==B[-1] and stack[-len(B)::]==list(B):
        flag=True
        for _ in range(len(B)):stack.pop()
if len(stack)==0: print("FRULA")
else:print(''.join(stack))