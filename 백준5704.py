while True:
    s = input()
    if s == '*': break
    D = {}
    for i in range(26):
        D[chr(97+i)] = 0 #key에는 아스키코드 a~z value는 0으로 초기화

    for i in range(len(s)):
        if 97<=ord(s[i])<=122: #s[i]가 알파벳 소문자인가?
            D[s[i]]+=1

    #처음엔 알파벳이 모두 있다고 가정하고 나중에 False로 변경
    flag = True
    key = list(D.keys())
    for i in range(len(key)):
        if D[key[i]] ==0 :
            flag = False
    if flag == True : print('Y')
    else : print("N")