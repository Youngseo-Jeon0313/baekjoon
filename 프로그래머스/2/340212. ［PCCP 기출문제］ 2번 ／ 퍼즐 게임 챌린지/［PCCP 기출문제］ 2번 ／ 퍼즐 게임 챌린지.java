class Solution {
    
    private long check(int num, int[] diffs, int[] times) {
        long temp_answer = 0;
        for (int i = 0; i < diffs.length; i++) {
            if (diffs[i] <= num) {
                temp_answer += times[i];
            } else {
                if (i > 0) {
                    temp_answer += ((long)diffs[i] - (long)num) * ((long)times[i] + (long)times[i - 1]) + (long)times[i];
                } else {
                    temp_answer += ((long)diffs[i] - (long)num) * (long)times[i] + (long)times[i];
                }
            }
        }
        return temp_answer;
    }

    
    public int solution(int[] diffs, int[] times, long limit) {
        int answer = 1;
        int left = 1; int right = 100000;
        
        while (left <= right){
            int mid = (left+right)/2;
            // System.out.println("mid: "+mid+" check값: "+check(mid, diffs, times));
            if (check(mid, diffs, times) <= limit){
                answer = mid; // 최대한 작아야 함
                right = mid-1;
            } else {
                left = mid+1; 
            }
        }
        return answer;
    }
}