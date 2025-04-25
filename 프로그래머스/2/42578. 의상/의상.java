import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        HashMap<String, ArrayList<String>> map = new HashMap<String, ArrayList<String>>();
        for (String[] cloth: clothes){
            if (map.containsKey(cloth[1])){
                map.get(cloth[1]).add(cloth[0]);
            } else{
                ArrayList<String> list = new ArrayList<String>();
                list.add(cloth[0]);
                map.put(cloth[1], list);
            }
        }
        int answer = 0;
        for (Map.Entry<String, ArrayList<String>> entry : map.entrySet()) {
            int size = entry.getValue().size();
            answer += answer * size + size;
        }
        return answer;
    }
}