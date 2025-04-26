import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        
        // 일단 큐로 만들자
        Queue<String> q = new LinkedList<>();
        for (int i=0; i<s.length(); i++){
            q.add(String.valueOf(s.charAt(i)));
        }
        
        // start_str 초기화
        String start_str = "";
        int left = 0;
        int right = 0;
        while (!q.isEmpty()){
            if (start_str.equals("")){
                // 여기는 시작하는 곳임
                start_str = q.poll();
                left += 1;
            } else {
                if (q.poll().equals(start_str)){
                    left+=1;
                } else {
                    right +=1;
                }
                if (left == right){
                    answer +=1;
                    left = 0;
                    right = 0;
                    start_str = "";
                }
            }
        }
        if (left!=right){
            answer +=1;
        }
        return answer;
    }
}