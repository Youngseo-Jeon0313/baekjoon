def check(s):
    stack = []
    for char in s:
        # print('char,', char, 'stack', stack)
        if char in ('(','[', '{'):
            stack.append(char)
        elif char in (')',']','}'):
            if char == ')' and stack and stack[-1]=='(':
                stack.pop()
            elif char == ']' and stack and stack[-1]=='[':
                stack.pop()
            elif char == '}' and stack and stack[-1]=='{':
                stack.pop()
            else:
                return False
    if stack: return False
    return True

def solution(s):
    answer = 0
    for i in range(len(s)):
        t = s[i:len(s)]+s[0:i]
        # print(t)
        if check(t):
            answer+=1
    return answer