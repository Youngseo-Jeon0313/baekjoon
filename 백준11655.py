
s=list(input())

for i in range(len(s)):
    if 65<=ord(s[i])<=90 or 97<=ord(s[i])<=122:
        if s[i].isupper(): #카이사르 대문자 version
            s[i]=chr(((ord(s[i]) - 65 + 26 - 13) % 26) + 65)
        else:     #카이사르 소문자 version
            s[i]=chr(((ord(s[i]) - 97 + 26 - 13) % 26) + 97)
        
    else:
        s[i]=s[i]
print(''.join(s))