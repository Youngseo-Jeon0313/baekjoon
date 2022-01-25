s=list(input())
key=input()


for i in range(len(s)):
    if s[i]==' ':
        continue
    tempo=ord(key[i%len(key)])-96
    s[i]=chr((ord(s[i])-tempo-97+26)%26+97)
    
print(''.join(s))