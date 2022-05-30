'''
최대힙이나 최소힙 만들 시 (튜플 형식)으로 넣는 것이 안정하다

'''


import sys
input=sys.stdin.readline
import heapq 
N=int(input())
leftheap=[]; rightheap=[]; #왼쪽힙은 최대힙으로 작은 애들을 넣을 거다
#오른쪽 힙은 최소힙으로 큰 애들을 넣을 거다.
heapq.heapify(leftheap);
heapq.heapify(rightheap);
answer=[]
for i in range(1,N+1):
    num=int(input())
    if len(leftheap)==len(rightheap):
        heapq.heappush(leftheap,(-num,num))
    else:
        heapq.heappush(rightheap,(num,num))
    #최대힙의 root는 가장 커야하고 최소힙의 root는 가장 작아야 하는데 그렇지 못할 경우
    # print('leftheap:',leftheap)
    # print('rightheap:',rightheap)
    #만약 최대힙의 최대값 > 최소힙의 최소값 이라면 바꿔줄 거다.
    if  len(rightheap)>0 and leftheap[0][1]>rightheap[0][1]:
        a=heapq.heappop(leftheap)[1]
        b=heapq.heappop(rightheap)[1]
        heapq.heappush(leftheap,(-b,b))
        heapq.heappush(rightheap,(a,a))
    # print('leftheap:',leftheap)
    # print('rightheap:',rightheap)
    print(leftheap[0][1])