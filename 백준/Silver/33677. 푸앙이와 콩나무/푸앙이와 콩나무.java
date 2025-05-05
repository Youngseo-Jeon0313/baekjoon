import java.io.*;
import java.util.*;


public class Main{
    public static void main(String ars[]) throws IOException{
        Set<Long> check = new HashSet<>();
        int[] answer = new int[2];
        answer[0] = Integer.MAX_VALUE;
        answer[1] = Integer.MAX_VALUE;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        Queue<Node> q = new LinkedList();
        q.add(new Node(0, 0, 0));

        while (!q.isEmpty()){
            Node now = q.poll();
            check.add(now.num);
            if (now.num == N){
                if (answer[0] >= now.depth){
                    answer[0] = now.depth;
                    if (answer[1] >= now.water){
                        answer[1] = now.water;
                    }
                }
            }
            if (now.num + 1<=N && !check.contains(now.num + 1)){
                q.offer(new Node(now.num + 1, now.depth+1, now.water+1));
            }
            if (now.num *3<=N && !check.contains(now.num * 3)){
                q.offer(new Node(now.num * 3, now.depth+1, now.water+3));
            }
            if (now.num*now.num <=N && !check.contains(now.num * now.num)){
                q.offer(new Node(now.num * now.num, now.depth+1, now.water+5));
            }
//            System.out.println(q);
        }
        bw.write(answer[0] + " " + answer[1]);
        bw.flush();
        bw.close();
    }
}

class Node{
    long num;
    int depth;
    int water;

    public Node(long num, int depth, int water){
        this.num = num;
        this.depth = depth;
        this.water = water;
    }
    @Override
    public String toString() {
        return "Node: "+num+','+depth+','+water;
    }
}