import java.util.*;

class Solution {
    public int[][] cost = {
        { 1, 7, 6, 7, 5, 4, 5, 3, 2, 3 },
        { 7, 1, 2, 4, 2, 3, 5, 4, 5, 6 },
        { 6, 2, 1, 2, 3, 2, 3, 5, 4, 5 },
        { 7, 4, 2, 1, 5, 3, 2, 6, 5, 4 },
        { 5, 2, 3, 5, 1, 2, 4, 2, 3, 5 },
        { 4, 3, 2, 3, 2, 1, 2, 3, 2, 3 },
        { 5, 5, 3, 2, 4, 2, 1, 5, 3, 2 },
        { 3, 4, 5, 6, 2, 3, 5, 1, 2, 4 },
        { 2, 5, 4, 5, 3, 2, 3, 2, 1, 2 },
        { 3, 6, 5, 4, 5, 3, 2, 4, 2, 1 }
    };
    public int[][][] dp; //dp[ind][left][right]
    public String arr;
    public int len;
    
    public int dfs(int L, int R, int depth){
        if (depth == len){
            return 0;
        }
         if (dp[depth][L][R] != -1) {
             return dp[depth][L][R];
         }

        int num = arr.charAt(depth) - '0';
        int result = Integer.MAX_VALUE;
        
        //left가 가게한다.
        if (num != R) result = Math.min(dfs(num, R, depth+1) + cost[L][num], result);
        //right가 가게 한다.
        if (num != L) result = Math.min(dfs(L, num, depth+1) + cost[R][num], result);
        return dp[depth][L][R] = result;
    }
    
    public int solution(String numbers) {
        arr = numbers;
        len = numbers.length();
        dp = new int[len+1][10][10];
        for (int i = 0; i < len + 1; i++) {
            for (int j = 0; j < 10; j++)
                Arrays.fill(dp[i][j], -1);
        }
        
        return dfs(4,6,0);
    }
}