#heapq 최소 힙 -- 노드!!!

import heapq

#모듈
heapq.heapify(iterable) #원래 있던 리스트를 힙으로 사용

#무조건 이 첫번째에 heap이 들어가야 함
heapq.heappush(heap, item) #heapify된 상태를 유지하면서 값 넣기

heapq.heappop(heap) #루트에 있는 값을 pop

#최대 힙 만들기
arr=[3,2,4,1,6,8,5]
heap=[]

for i in arr:
    heapq.heappush(heap, (-i,i))

print(heap)
while heap:
    print(heapq.heappop(heap)[1], end=" ")
    

#만약 from heapq import * 이렇게 표기한다면 굳이 heapq.~~ 이렇게 안 하고 바로
#heapify(hq) 이런 식으로 가면 됨!!!!



#시간 복잡도 NlogN -최소

#만약 내림차순으로 하고 싶다면 value=> -value, append(-~~) 이렇게 -로 넣고 -로 빼면 된다.