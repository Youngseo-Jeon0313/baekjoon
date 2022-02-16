'''

t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    print(a**b%10)
이렇게 하면 시간초과가 뜬다ㅠㅠ b가 1000000까지 갈 수 있기 때문인디,
그래서 규칙성을 찾아서 구현해야 한다ㅠㅠ    
'''
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    a=a%10
    c=b%4 #규칙성이 4
    if c==0: c=4
    d=b%3 #규칙성이 3 인 건 없음ㅎㅎ..
    e=b%2
    if e==0: e=2
    if a==1: print(1)
    elif a==2: print(2**c%10)
    elif a==3: print(3**c%10)
    elif a==4: print(4**e%10)
    elif a==5: print(5)
    elif a==6: print(6)
    elif a==7: print(7**c%10)
    elif a==8: print(8**c%10)
    elif a==9: print(9**e%10)
    else: print(10)