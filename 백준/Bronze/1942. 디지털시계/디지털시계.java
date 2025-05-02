import java.util.*;
import java.io.*;

public class Main
{
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        for (int i=0; i<3; i++){
            String[] input = br.readLine().split(" ");
            String[] start = input[0].split(":");
            String[] end = input[1].split(":");

            int h1 = Integer.parseInt(start[0]);
            int m1 = Integer.parseInt(start[1]);
            int s1 = Integer.parseInt(start[2]);

            int h2 = Integer.parseInt(end[0]);
            int m2 = Integer.parseInt(end[1]);
            int s2 = Integer.parseInt(end[2]);

            int answer = 0;
            while (true){
                if (s1 == 60){
                    m1 += 1;
                    s1 = 0;
                }
                if (m1 == 60){
                    h1 += 1;
                    m1 = 0;
                }
                if (h1 == 24){
                    h1 = 0;
                }
                int x = h1 + m1 + s1;
                if (x%3 == 0){
                    answer += 1;
                }
                if (h1 == h2 && m1 == m2 && s1 == s2){
                    break;
                }
                s1 +=1;
            }
            bw.write(answer + "\n");
        }
        bw.flush();
        bw.close();
    }
}