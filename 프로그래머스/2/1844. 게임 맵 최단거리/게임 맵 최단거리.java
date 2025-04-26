import java.util.*;

class Solution {
    int[] dx = {1,0,-1,0};
    int[] dy = {0,1,0,-1};
    int[][] check;
    
    public int solution(int[][] maps) {
        check = new int[maps.length][maps[0].length];
        for (int i=0; i<maps.length; i++){
            Arrays.fill(check[i], Integer.MAX_VALUE);
        }
        int answer = 0;
        
        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(0,0,1));
        
        while (!q.isEmpty()){
            Node node = q.poll();
            check[node.y][node.x] = node.depth;
            for (int i=0; i<4; i++){
                int nx = node.x + dx[i];
                int ny = node.y + dy[i];
                
                if (0<=nx && nx<maps[0].length && 0<=ny && ny<maps.length){
                    if (maps[ny][nx]==0){
                        continue;
                    }
                    if (node.depth+1 < check[ny][nx]){
                        q.offer(new Node(ny, nx, node.depth+1));
                        check[ny][nx]=node.depth+1;
                    }
                }
            }     
        }
        if (check[maps.length-1][maps[0].length-1] == Integer.MAX_VALUE){
            return -1;
        }
        return check[maps.length-1][maps[0].length-1];
    }
}

class Node{
    int y;
    int x;
    int depth;
    
    public Node(int y, int x, int depth){
        this.y = y;
        this.x = x;
        this.depth = depth;
    }
}