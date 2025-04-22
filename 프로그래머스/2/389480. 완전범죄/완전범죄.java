
class Solution {
    public int solution(int[][] info, int n, int m) {
        int answer = (int)1e6;
        // DP[a점수][b점수]=True/False
        boolean[][] DP = new boolean[140][140];
        // System.out.println(DP);
        // 모두 False로 초기화
        for (int i=0; i<140; i++){
            for (int j=0; j<140; j++){
                DP[i][j] = false;
            }
        }
        DP[0][0]=true;
        for (int i=0; i<info.length ; i++){
            boolean[][] new_DP = new boolean[140][140];
            boolean check = false;
            for (int a=0; a<140; a++){
                for (int b=0; b<140; b++){
                    if (DP[a][b]){
                        if (a+info[i][0] < n){
                            new_DP[a+info[i][0]][b]=true;
                        }
                        if (b+info[i][1] < m){
                            new_DP[a][b+info[i][1]] = true;
                        }
                        
                    }
                }
            }
            // DP를 new_DP로
            for (int a=0; a<140; a++){
                for (int b=0; b<140; b++){
                    DP[a][b] = new_DP[a][b];
                }
            }
        }
        for (int x=0; x<140; x++){
                for (int y=0; y<140; y++){
                    if (DP[x][y]) {
                        answer = Math.min(answer, x);
                    }
                }
            }
        if (answer == (int)1e6){
            return -1;
        }
        return answer;
    }
}