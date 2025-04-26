import java.util.*;

class Solution {
    public int solution(int N, int[][] road, int K) {
        int[] cost = new int[N+1];
        
        ArrayList<Node>[] adj = new ArrayList[N+1];
        for (int i = 0; i <= N; i++) {
            adj[i] = new ArrayList<>();
            cost[i] = Integer.MAX_VALUE;
        }
        for (int i=0; i<road.length; i++){
            adj[road[i][0]].add(new Node(road[i][1], road[i][2]));
            adj[road[i][1]].add(new Node(road[i][0], road[i][2]));
        }
        
        PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2)-> {
            return o1.cost - o2.cost;
        });
        
        pq.offer(new Node(1,0));
        while (!pq.isEmpty()){
            Node node = pq.poll();
            if (cost[node.node] < node.cost) continue;
            cost[node.node] = node.cost;
            for (Node nextNode: adj[node.node]){
                if (cost[nextNode.node] > node.cost + nextNode.cost){
                    cost[nextNode.node] = node.cost + nextNode.cost;
                    pq.offer(new Node(nextNode.node, cost[nextNode.node]));
                }
            }
        }
        
        int answer = 0;
        for (int i = 0; i <= N; i++) {
            if (cost[i]<=K){
                answer +=1;
            } 
        }        
        return answer;
    }
}

class Node{
    int node;
    int cost;
    
    public Node(int node, int cost){
        this.node = node;
        this.cost = cost;
    }
}