'''
이중우선순위큐
<해결방법>
최대힙 & 최소힙 두 개를 만들어서 해결
I n : 정수 n을 Q에 삽입
D 1 : Q에서 최댓값 삭제 -> 두 개 이상이면 하나만★ 삭제
D -1: Q에서 최솟값 삭제
--만약 Q가 비어있으면 D연산 무시 가능

생각::최소힙에서 뺄 때 혹은 최대힙에서 뺄 때 동시에 빼야 함 ㅠㅠ
'''
import sys
input=sys.stdin.readline

import heapq
t=int(input())
for i in range(t):
    max_heap=[]; min_heap=[]
    num=int(input())
    Check=[False]*num
    for i in range(num):
        method, much=input().split()
        if method=='I':
            heapq.heappush(min_heap,[int(much),i])
            heapq.heappush(max_heap,[-int(much),i])
            Check[i]=True
        else:
            if much=='-1':
                while min_heap:
                    s=heapq.heappop(min_heap)
                    if Check[s[1]]==True:
                        Check[s[1]]=False; break
            elif much=='1':
                while max_heap:
                    t=heapq.heappop(max_heap)
                    if Check[t[1]]==True:
                        Check[t[1]]=False; break
    
    FLAG=True
    while max_heap:
        a=heapq.heappop(max_heap)
        if Check[int(a[1])]:
            FLAG=False; print(-a[0], end=' '); break 

    while min_heap:
        b=heapq.heappop(min_heap)  
        if Check[int(b[1])]:
            FLAG=False; print(b[0]); break
    if FLAG==True: print('EMPTY')