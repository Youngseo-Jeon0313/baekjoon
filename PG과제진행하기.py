from collections import deque

def solution(plans):
    # 남으면 스택에 넣는다. (뒤에 있을수록 가장 최근에 멈춘 과제)
    stack = []
    answer = []
    # 우선 먼저 시작하는 순서대로 정렬
    plans=sorted(plans, key = lambda x:x[1])
    # 현재 시각
    now = 0
    # 하나씩 살펴보기
    for i in range(len(plans)): 
        if i == len(plans)-1: 
            answer.append(plans[i][0]); 
            for j in range(len(stack)-1,-1,-1):
                answer.append(stack[j][0]); 
            continue
        
        check = plans[i][1]
        hour, minute = map(int,check.split(':'))
        check_time = hour*60+minute
        
        next = plans[i+1][1]
        next_hour, next_minute = map(int,next.split(':'))
        next_time = next_hour*60+next_minute
        
        if (next_time - check_time) < int(plans[i][2]): 
            stack.append([plans[i][0],int(plans[i][2])-(next_time-check_time)])
        
        # 다른 애들을 해줄 수 있다.
        else:
            answer.append(plans[i][0])
            possible_time = next_time-(int(plans[i][2])+check_time)
            while stack and possible_time:
                temp_time = stack.pop()
                temp_time[1]=int(temp_time[1])
                if possible_time >= temp_time[1]:
                    answer.append(temp_time[0])
                    possible_time-=temp_time[1]
                else: 
                    stack.append([temp_time[0], temp_time[1]-possible_time])
                    possible_time=0
        
    return answer


