import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        long[][] dp = new long[90+1][2];

        // Initialize base cases
        dp[1][0] = 0; dp[1][1] = 1;
        dp[2][0] = 1; dp[2][1] = 0;
        dp[3][0] = 1; dp[3][1] = 1;

        // DP transitions
        for (int i = 3; i < N; i++) {
            dp[i+1][0] = dp[i][0] + dp[i][1];
            dp[i+1][1] = dp[i][0];
        }

        // Output the result
        System.out.println(dp[N][0] + dp[N][1]);
    }
}
