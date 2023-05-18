from collections import deque

def solution(boxes, m,k):

    answer = m
    boxes =sorted(boxes,reverse=True)
    deq = deque(boxes)
    while deq and k:
        top=deq[0]
        if m//10000 * top <= 100000: 
            answer += m//10000 * top 
            m+= m//10000 * top 
            k-=1
        else: deq.popleft()
        
    return answer


print(solution([1000,800,900],1000000,3))
print(solution([9000,10000,8520,9500],110000,4))



import java.util.*;


public int solution(int[] boxes, int m, int k) {
    int answer = m;
    Arrays.sort(boxes);
    Deque<Integer> deq = new ArrayDeque<Integer>();
    for(int box : boxes) {
        deq.push(box);
    }
    while(!deq.isEmpty() && k > 0) {
        int top = deq.peekFirst();
        if(m / 10000 * top <= 100000) {
            answer += m / 10000 * top;
            m += m / 10000 * top;
            k--;
        } else {
            deq.pollFirst();
       }
    }
    return answer;
}