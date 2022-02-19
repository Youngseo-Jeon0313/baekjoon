'''
시간초과 문제가 생긴다.
이유는 내가 R을 마주칠 때마다 reverse를 해주다보면 너무 많이 쓰기 때문 ㅠㅠ
그래서 reverse는 마지막에 '들어있는 R의 개수가 짝수인가?를 기준으로
짝수면 안 뒤집어줘도 되고 홀수면 뒤집어줘야 한다.
그러면 D를 할 때 문제가 생기게 되는데 D를 할 때는 R의 개수가 D전에 몇 개 나왔는가에 따라서
만약 R이 짝수번 나왔으면 그냥 popleft를, 홀수번 나왔을 때는 pop을 하면 된다.
'''
from collections import deque

t=int(input())
for i in range(t):
    flag=True
    f=input()
    num=int(input())
    s=deque(input().split(','))
    s[0]=s[0][1:]
    s[num-1]=s[num-1][:-1]
    R_num=0
    for j in f:
        if j=='R': R_num+=1
        else: 
            if len(s)>0 and s!=deque(['']) : 
                if R_num%2==0:s.popleft()
                else:s.pop()
            else: flag=False; print('error'); break;
    if R_num%2!=0: s.reverse()
    if flag==True:
        print('[',end='')
        print(','.join(s),end='')
        print(']')
