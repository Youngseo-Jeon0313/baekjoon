from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    deq = deque(bridge_length * [0])

    temp_sum = 0
    while deq:
        answer+=1
        temp_sum-=deq.popleft()
        if truck_weights :
            if temp_sum + truck_weights[0] <= weight:
                truck = truck_weights.pop(0)
                deq.append(truck)
                temp_sum+=truck
                
            else: deq.append(0)
    return answer