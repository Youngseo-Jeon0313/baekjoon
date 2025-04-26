import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>((o1, o2)-> {
            return o1 - o2;
        });
        for (int s: scoville){
            pq.offer(s);
        }
        
        while (pq.size() > 1){
            // System.out.println(pq);
            if (pq.peek() < K){
                int first = pq.poll();
                int second = pq.poll();
                pq.offer(first + second*2);
                answer += 1;
            } else {
                break;
            }
        }
        if (pq.peek() < K){
            return -1;
        } else {
            return answer;
        }
    }
}