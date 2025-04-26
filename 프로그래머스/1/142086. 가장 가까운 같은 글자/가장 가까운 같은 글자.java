import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        HashMap<String, Integer> map = new HashMap<>();
        
        for (int i=0; i<s.length(); i++){
            if (map.containsKey(String.valueOf(s.charAt(i)))){
                answer[i]=i+1-map.get(String.valueOf(s.charAt(i)));
                map.put(String.valueOf(s.charAt(i)), i+1);
            } else {
                answer[i]=-1;
                map.put(String.valueOf(s.charAt(i)), i+1);
            }
        }
        return answer;
    }
}