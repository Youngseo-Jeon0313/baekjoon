class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        for (int i=0; i<=t.length()-p.length(); i++){
            String a = t.substring(i,i+p.length());
            // System.out.println(a);
            if (Long.parseLong(a) <= Long.parseLong(p)){
                answer+=1;
            }
        }
        return answer;
    }
}