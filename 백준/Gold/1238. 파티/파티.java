import java.util.*;
import java.io.*;

public class Main{

    static int n, w, x;
    static List<List<Edge>> adj;
    static final int INF = Integer.MAX_VALUE;

    static int[] dijkstra(int start){
        int[] cost = new int[n + 1];
        Arrays.fill(cost, INF);
        PriorityQueue<int[]> pq = new PriorityQueue<>(
                (a, b) -> { return a[1] - b[1]; }
        );
        pq.offer(new int[]{start, 0}); // node, cost
        cost[start] = 0;

        while (!pq.isEmpty()){
            int[] cur = pq.poll();
            int curNode = cur[0];
            int curCost = cur[1];

            if (curCost > cost[curNode]){
                continue; // 이미 방문
            }

            for (Edge edge : adj.get(curNode)){
                int nextNode = edge.nextNode;
                int nextCost = curCost + edge.cost;

                if (nextCost < cost[nextNode]){
                    cost[nextNode] = nextCost;
                    pq.offer(new int[]{nextNode, nextCost});
                }
            }
        }
        return cost;
    }

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        w = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());

        adj = new ArrayList<>();
        //init
        for (int i=0; i<n+1; i++){
            adj.add(new ArrayList<>());
        }

        for (int i=0; i<w; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            adj.get(a).add(new Edge(b, c));
        }

        int[] timeStart = new int[n + 1];
        for (int i=1; i<=n; i++){
            int[] time = dijkstra(i);
            timeStart[i] = time[x];
        }

        int[] timeEnd = dijkstra(x);
        int result = 0;

        for (int i=1; i<=n; i++){
            if (timeStart[i] != INF && timeEnd[i] != INF){
                result = Math.max(result, timeStart[i] + timeEnd[i]);
            }
        }
        System.out.println(result);
    }

    static class Edge {
        int nextNode, cost;

        Edge(int nextNode, int cost) {
            this.nextNode = nextNode;
            this.cost = cost;
        }
    }
}
