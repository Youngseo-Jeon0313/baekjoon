while True:
    s=input()
    if s== '#': break

    x =-1
    for i in range(len(s)):
        if s[i] in ['a','e','i','o','u']:
            x=i
            break
#모음과 탁 마주치는 순간 멈추고
#slice!

    if x!= -1:print(s[x:] +s[:x]+'ay')
    else: print(s+'ay')