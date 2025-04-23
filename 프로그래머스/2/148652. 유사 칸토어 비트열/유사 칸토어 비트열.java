class Solution {
    public int solution(int n, long l, long r) {
        int answer = 0;
        
        for (long i=l-1; i<r; i++){
            if (cantor(i) > 0){
                answer += 1;
            }
        }
        return answer;
    }
    public int cantor(long num){
        if (num % 5 == 2){
            return 0;
        }
        else if (num < 5){
            return 1;
        }
        return cantor(num / 5);
    }
}