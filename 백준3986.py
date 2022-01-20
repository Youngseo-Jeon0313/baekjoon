'''
구현 생각??
어차피 A랑 B로만 이루어진 단어이기 때문에
스택에 넣고 빼면서 판단하자.

이때 스택에 '아무것도없으면' 좋은 단어로 판단!
왜냐면 꼬이는 스텝이 없기 때문에
'''


n = int(input())
ans = 0
for i in range(n):
    s = input()
    stack = []
    for j in range(len(s)):
        if len(stack) == 0: stack.append(s[j])
        else:
            if stack[-1] == s[j]: stack.pop()
            else: stack.append(s[j])
    if len(stack) == 0: ans += 1
print(ans)