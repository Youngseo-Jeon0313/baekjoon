import sys
input=sys.stdin.readline

def solution(N, times):
    answer=0
    start=0; end=max(times) * N;
    while start<=end: #이분탐색 구간을 나오면 
        mid=(start+end)//2
        #조건
        standard=0
        for i in times:
            standard+=mid//i
        if standard>=N:
            answer=mid
            end=mid-1
        else :
            start=mid+1
        
    return answer
print(solution(6,[7,10]))