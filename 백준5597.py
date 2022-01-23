stack=[]
for i in range(1,31):
    stack.append(i)

for i in range(28):
    a=int(input())
    for j in range(30):
        if stack[j]==a:
            stack.pop(j)
            break

stack.sort()
print(stack[0])
print(stack[1])