import java.util.*;
import java.io.*;

class Main{
    static int[] prefix_sum;
    static int N;
    static int K;
    static int X;
    static int answer = 0;

    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        prefix_sum = new int[N+1];
        for (int i=0; i<N; i++){
            prefix_sum[i+1] = prefix_sum[i] + arr[i];
        }
//        System.out.println(Arrays.toString(prefix_sum));

        int left = 0; int right = N-1;
        while (left<=right){
            int mid = (left+right)/2;
            if (func(mid)) {
                // 가능하니까 더 길이 늘려도 됨
                answer = mid;
                left=mid+1;
            } else {
                right=mid-1;
            }
        }
        if (answer == 0){
            answer = -1;
        }
        bw.write(answer+"");
        bw.flush();
        bw.close();
    }
    public static boolean func(int width){
        for (int start=0; start<=N-width; start++){
            if ((long) X * prefix_sum[start] + prefix_sum[N] - prefix_sum[start+width] >= K){
                return true;
            }
        }
        return false;
    }
}