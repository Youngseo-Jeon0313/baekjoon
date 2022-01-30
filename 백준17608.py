'''
시간 초과가 나니까 
pop이나 reverse는 굳이..



import sys
input=sys.stdin.readline


N=int(input())
Box=[]
for i in range(N):
    s=int(input())
    #애초에 여기서 거꾸로 들어가면 오류가 덜 남
    if len(Box)>0:
        for i in range(len(Box)-1,-1,-1):
            if int(Box[i])<=s:
                Box.pop(i)
    Box.append(s)
print(len(Box))

'''

import sys
input=sys.stdin.readline

N=int(input())
Box=[]
for i in range(N):
    s=int(input())
    Box.append(s)
visible_stick=1
length=Box[-1]
for i in range(N-1,-1,-1):
    if Box[i]>length:
        visible_stick+=1
        length=Box[i]
print(visible_stick)