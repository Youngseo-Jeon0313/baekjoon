class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        String answer = "";
        // 모두 분으로 바꾸자.
        int videoLen = Integer.valueOf(video_len.split(":")[0])*60+Integer.valueOf(video_len.split(":")[1]);
        int poS = Integer.valueOf(pos.split(":")[0])*60+Integer.valueOf(pos.split(":")[1]);
        int opStart = Integer.valueOf(op_start.split(":")[0])*60+Integer.valueOf(op_start.split(":")[1]);
        int opEnd = Integer.valueOf(op_end.split(":")[0])*60+Integer.valueOf(op_end.split(":")[1]);
        
        for (String command: commands){
            if (opStart<=poS && poS<=opEnd){
                poS = opEnd;
            }
            if (command.equals("next")){
                poS = Math.min(poS+10, videoLen);
            } else if (command.equals("prev")){
                poS = Math.max(poS-10, 0);
            }
        }
        if (opStart<=poS && poS<=opEnd){
            poS = opEnd;
        }
        System.out.println(poS);
        if (poS/60<10){
            answer+="0";
        }
        answer+=String.valueOf(poS/60);
        answer+=":";
        if (poS%60<10){
            answer+="0";
        }
        answer+=String.valueOf(poS%60);
        return answer;
    }
}