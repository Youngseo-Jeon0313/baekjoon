from collections import deque



n=int(input())

one_time=deque() #1번팀이 이기는 시간
two_time=deque()
flag=0
for i in range(n):
    team, time=input().split()
    m,s=map(int, time.split(':'))
    if team=='1':
        flag+=1
        one_time.append(60*m+s)
        if len(two_time)>1:
            two_time.pop()
        elif len(two_time)==1 and flag==0:
            x=two_time.pop()
            two_time.append((60*m+s)-x)

    else: 
        flag-=1
        two_time.append(60*m+s)
        if len(one_time)>1:
            one_time.pop()
            continue
        if len(one_time)==1 and flag==0:
            x=one_time.pop()
            one_time.append(60*m+s-x)
print(one_time)
print(two_time)
#끝났을 때 무승부로 끝남


'''



if len(one_time)==1:
    print(one_time[0])
if len(two_time)==1:
    print(two_time[0])
if len(one_time)>1:
    print(48*60-one_time[1])
if len(two_time)>1:
    print(48*60-two_time[1])
'''