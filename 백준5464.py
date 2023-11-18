import heapq
"빡구현 + heapq + deque"
from collections import deque

answer = 0
N, M = map(int,input().split())
car_center = [] # index - 주차장 번호 / 값 - 주차료 -> 이후 최종 주차료는 차 무게 * 주차료
for _ in range(N):
    car_center.append(int(input()))

cars = [] # index - 차 번호 / 값 - 차 무게
for _ in range(M):
    cars.append(int(input()))

heap = [i for i in range(N)] #주차장들
car_center_car_index = ['' for _ in range(N)]
deq = deque([])
for _ in range(2*M):
    #print(heap)
    action = int(input())
    if action>0: #들어오는 것이라면
        action-=1
        if len(heap)==0:
            #대기시킨다.
            deq.append(action)
        else:
            index = heapq.heappop(heap) #여기에 대겠다.
            car_center_car_index[index]= action
            answer += car_center[index]*cars[action]
    else:
        action+=1
        car_center_index = car_center_car_index.index(-action)
        heapq.heappush(heap,car_center_index)
    if deq and heap:
        while heap and deq:
            action = deq.popleft()
            index = heapq.heappop(heap) #여기에 대겠다.
            car_center_car_index[index]= action
            answer += car_center[index]*cars[action]
print(answer)