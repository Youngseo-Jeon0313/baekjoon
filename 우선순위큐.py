#heapq 최소 힙 -- 노드!!!

import heapq

def heapsort(iterable): #iterable은 list나 tuple같은 것
    h = []
    result = []
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value) #넣을 때 
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h)) #꺼낼 때
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

#시간 복잡도 NlogN -최소

#만약 내림차순으로 하고 싶다면 value=> -value, append(-~~) 이렇게 -로 넣고 -로 빼면 된다.