stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1])
print(stack)

#스택구조를 구현하기 위해서는 list와 append, pop 함수를 이용하면 된다.