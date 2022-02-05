t=int(input())
for i in range(t):
    s=input()
    l=len(s)
    if s[l//2-1]==s[l//2]:
        print('Do-it')
    else:
        print('Do-it-Not')