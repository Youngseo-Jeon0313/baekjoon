s=input()
s+='1'

for i in range(len(s)):
    if s[i+1]==s[i] :
        print(1)