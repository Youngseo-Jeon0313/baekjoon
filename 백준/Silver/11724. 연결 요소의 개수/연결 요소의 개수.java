import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int answer = 0;
        boolean[] check = new boolean[N+1];
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for (int i=0; i<=N; i++){
            adj.add(new ArrayList<Integer>());
        }

        for (int i=0; i<M; i++){ // a -> b 로 연결되어 있음
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            adj.get(a).add(b);
            adj.get(b).add(a);
        }
        Queue<Integer> q = new LinkedList<>();
        for (int i=1; i<=N; i++){
            if (!check[i]){
                answer +=1;
                q.offer(i);
                check[i]=true;
                while (!q.isEmpty()){
                    int node = q.poll();
                    for (int j=0; j<adj.get(node).size(); j++){
                        if (!check[adj.get(node).get(j)]){
                            q.offer(adj.get(node).get(j));
                            check[adj.get(node).get(j)] = true;
                        }
                    }
                }
            }
        }
        bw.write(answer+"");
        bw.flush();
        bw.close();
    }
}