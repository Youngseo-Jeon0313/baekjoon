import java.util.*;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = new int[photo.length];
        HashMap<String, Integer> scores = new HashMap<>();
        for (int i=0; i<name.length; i++){
            scores.put(name[i], yearning[i]);
        }
        for (int j=0; j<photo.length; j++){
            for (int k=0; k<photo[j].length; k++){
                if (scores.containsKey(photo[j][k])){
                    answer[j]+=scores.get(photo[j][k]);
                }
            }
        }
        
        
        return answer;
    }
}