'''
for문으로 하면 문제는 
pop할 때 글자 len이 줄어드는 문제이다.

'''

s=input()

S='CAMBRIDGE'
s=list(s)
ss=len(s)
j=0
i=0
check=0

while True:
    if s[i] in S:
        i+=1
    else:
        print(s[i],end='')
        i+=1
    if i==len(s):
        break