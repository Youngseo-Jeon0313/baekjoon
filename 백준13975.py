
'''
푸는 방법
1. 파일 중에서 가장 작은 두 개를 뽑는다.
2. 합친다.
3. 합친 걸 다시 파일들에 둔다.
4. 반복

heappush:그냥 맨 뒤에 붙여줌
heappop:우선순위가 높은★ 요소를 먼저 처리(가장 작은)
'''
import sys
input = sys.stdin.readline
import heapq

t=int(input())
for i in range(t):
    num=int(input())
    arr=list(map(int,input().split()))
    sum=0
    q=[]
    for i in arr:
        heapq.heappush(q,i)
    while len(q)>1:
        a=heapq.heappop(q)
        b=heapq.heappop(q)
        heapq.heappush(q,a+b)
        sum+=a+b
    print(sum)
