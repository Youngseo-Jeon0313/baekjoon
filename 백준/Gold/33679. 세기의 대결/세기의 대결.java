import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] YJ = new int[N];
        int[] check_YJ = new int[N];
        int YJ_score = 0;
        int[] HG = new int[N];
        int[] check_HG = new int[N];
        int HG_score = 0;

        for (int i=0; i<N; i++){
            YJ[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++){
            HG[i] = Integer.parseInt(st.nextToken());
        }

        // 회전을 고려해야 함
        for (int start = 0; start < N; start++){
            Arrays.fill(check_YJ, 1);
            Arrays.fill(check_HG, 1);

            int[] new_YJ = new int[N];
            int[] new_HG = new int[N];

            for (int i=0; i<N; i++){
                new_YJ[i] = YJ[(start+i)%N];
                new_HG[i] = HG[(start+i)%N];
            }

//            System.out.println(Arrays.toString(new_YJ));
//            System.out.println(Arrays.toString(new_HG));


            for (int i=0; i<N; i++){
                for (int j=0; j<i; j++){
                    if (new_YJ[j] < new_YJ[i]){
                        check_YJ[i] = Math.max(check_YJ[i], check_YJ[j]+1);
                        YJ_score = Math.max(YJ_score, check_YJ[i]);
                    }
                    if (new_HG[j] < new_HG[i]){
                        check_HG[i] = Math.max(check_HG[i], check_HG[j]+1);
                        HG_score = Math.max(HG_score, check_HG[i]);
                    }
                }
            }
        }



        if (YJ_score < HG_score){
            bw.write("HG Win!");
        } else if (YJ_score > HG_score) {
            bw.write("YJ Win!");
        } else {
            bw.write("Both Win!");
        }

        bw.flush();
        bw.close();
    }
}