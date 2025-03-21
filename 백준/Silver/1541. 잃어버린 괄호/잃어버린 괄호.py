from collections import deque
str_ = input()
S=[]
deq = deque(list(str_))
temp_str = ''
while deq:
    a = deq.popleft()
    if a=='+':
        if temp_str: 
            S.append(temp_str)
            temp_str = ''
        S.append('+')
    elif a=='-':
        if temp_str: 
            S.append(temp_str)
            temp_str = ''
        S.append('-')
    else:
        temp_str+=a
if temp_str: 
    S.append(temp_str)
    temp_str = ''
stack = []
num = 0
operator = '+'
# print('S',S)
for i in S:
    if i =='+':
        operator = '+'
    elif i == '-':
        stack.append(num)
        stack.append('-')
        operator = '-'
        num = 0
    else:
        num += int(i)
if num: stack.append(num)

final = ''
for item in stack:
    final += str(item)
print(eval(final))