from collections import deque
def solution(order):
    answer = 0
    container_belt = deque([i+1 for i in range(len(order))])
    stack = []
    index = 0
    while index<len(order):
        # print('index:',index,'answer:',answer, 'stack:', stack)
        if stack and stack[-1]==order[index]:
                stack.pop()
                index+=1
                answer+=1
        elif container_belt and container_belt[0] == order[index]:
            container_belt.popleft()
            index+=1
            answer+=1
        else:
            if container_belt:
                stack.append(container_belt.popleft())
            else: break
    return answer