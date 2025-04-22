import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        int now = 0; // 현재 시각
        int lastStart = -1; // 마지막 완료 시각
        int finishedJobCount = 0;
        int finishedJobReturnTime = 0;

        // 우선순위 큐 (소요 시간 기준으로 정렬)
        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (a, b) -> a[0] - b[0]  // a[0]은 작업 소요 시간
        );

        boolean[] visited = new boolean[jobs.length];

        while (finishedJobCount < jobs.length) {
            for (int i = 0; i < jobs.length; i++) {
                int start = jobs[i][0];
                int length = jobs[i][1];

                if (!visited[i] && lastStart < start && start <= now) {
                    pq.offer(new int[]{length, start, i});
                    visited[i] = true;
                }
            }

            if (!pq.isEmpty()) {
                int[] job = pq.poll(); // [length, start, index]
                int duringTime = job[0];
                int startTime = job[1];
                lastStart = now;
                now += duringTime;
                finishedJobReturnTime += now - startTime;
                finishedJobCount++;
            } else {
                now += 1;
            }
        }

        return finishedJobReturnTime / jobs.length;
    }
}
