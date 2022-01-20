n=int(input())
s=list(input())

if len(s)%2==0:
    for i in range(len(s)//2):
        if s[i] =='?':
            if s[len(s)-1-i] =='?':
                s[i]='a'
                s[len(s)-1-i]='a'
            else:
                s[i]=s[len(s)-1-i]
        if s[len(s)-1-i]=='?':
            if s[i] =='?':
                s[len(s)-1-i]='a'
                s[len(s)-1-i]='a'
            else:
                s[len(s)-1-i]=s[i]

    print(''.join(s))

else:
    for i in range(len(s)//2+1):
        if s[i] =='?':
            if s[len(s)-1-i] =='?':
                s[i]='a'
                s[len(s)-1-i]='a'
            else:
                s[i]=s[len(s)-1-i]
        if s[len(s)-1-i]=='?':
            if s[i] =='?':
                s[len(s)-1-i]='a'
                s[len(s)-1-i]='a'
            else:
                s[len(s)-1-i]=s[i]

    print(''.join(s))