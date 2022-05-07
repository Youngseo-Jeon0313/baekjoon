from collections import deque
def solution(queue1, queue2):
    queue1=deque(queue1)
    queue2=deque(queue2)
    if (sum(queue1)+sum(queue2))%2==1:return -1
    goal=(sum(queue1)+sum(queue2))//2
    if sum(queue1)==goal:return 0
    elif sum(queue1)>goal:
        GOAL=sum(queue1)-goal #얘를 0으로 만드는 것이 목표
        i=0; j=0; answer=0
        while i<=len(queue1) or j<=len(queue2):
            if GOAL==0: return answer
            elif GOAL>0:
                x=queue1.popleft()
                GOAL-=x
                queue2.append(x)
                answer+=1; i+=1
            else:
                x=queue2.popleft()
                GOAL+=x
                queue1.append(x)
                answer+=1; j+=1
        return -1
    else:
        GOAL=sum(queue2)-goal #얘를 0으로 만드는 것이 목표
        i=0; j=0; answer=0
        while i<len(queue2) or j<len(queue1):
            if GOAL==0: return answer
            elif GOAL>0:
                x=queue2.popleft()
                GOAL-=x
                queue1.append(x)
                answer+=1; i+=1
            else:
                x=queue1.popleft()
                GOAL+=x
                queue2.append(x)
                answer+=1; j+=1
        return -1

print(solution([3, 2, 7, 2],[4, 6, 5, 1]))
print(solution([1, 2, 1, 2],[1, 10, 1, 2]))
print(solution([1, 1],[1, 5]))