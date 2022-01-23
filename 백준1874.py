'''
망했다...
자꾸 시간초과 난다ㅠㅠㅠ
스택 하나에 입력된 수를 넣었다가 top이 입력한 수와 맞으면 pop하도록 하기

포인트는
바로나왔을 때랑 // 넣고 빠다가 나올 때를 다르게 취급하는 것
'''

import sys
input=sys.stdin.readline

n=int(input())
stack=[0]
PRINT=[]
'''

List=4 3 6 8 7 5 2 1
'''
j=1
for i in range(1,n+1):
    flag=True
    a=int(input())
    if stack[-1]<a: #만약에 stack안에 내가 목표하는 값보다 작은 것밖에 없어
        while stack[-1]<=a:
            stack.append(j)
            PRINT.append('+')
            if stack[-1]==a:
                PRINT.append('-')
                j+=1
                stack.pop()
                break
            else:
                j+=1
    elif stack[-1]==a: #만약에 내가 딱 목표한 게 딱 있어
        PRINT.append('-')
        stack.pop()
    else:
        while stack[-1]>=a:
            stack.pop()
            PRINT.append('-')
            if flag==False:
                print('NO')
                exit()
            flag=False


for i in PRINT:
    print(i)