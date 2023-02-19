import sys
input=sys.stdin.readline

#타일은 회전시킬 수 없다.!!


t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    for i in range(c):
        if b and a: 
            b-=1; a-=1
        elif a:
            a-=3
        else:
            print("No"); break
    while b>0:
        if b>1:
            b-=2
        elif a>1:
            b-=1; a-=2
        else:
            print("No");break
    if a%2:
        print("No")
    else:
        print("Yes")
