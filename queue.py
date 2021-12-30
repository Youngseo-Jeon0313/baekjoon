from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

#큐는 따로 프레임을 가져와서 해야 한다.
#먼저 들어오는 사람이 먼저 나옴