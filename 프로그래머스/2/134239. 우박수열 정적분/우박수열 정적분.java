import java.util.*;

class Solution {
    public double[] solution(int k, int[][] ranges) {
        ArrayList<Integer> heights = new ArrayList<>();
        ArrayList<Double> prefixSum = new ArrayList<>();
        while (k>1){
            heights.add(k);
            if (k%2 ==0){
                k /= 2;
            } else {
                k = k*3 +1;
            }
        }
        heights.add(1);
        // 구간 합 저장하기
        prefixSum.add(0d);
        for (int i=0; i<heights.size()-1; i++){
            prefixSum.add(prefixSum.get(i)+(heights.get(i)+heights.get(i+1))/2d);
        }
        // System.out.println(prefixSum);
        // answer에 담기
        double[] answer = new double[ranges.length];
        for (int j=0; j<ranges.length; j++){
            if (prefixSum.size()-1+ranges[j][1] < ranges[j][0]){
                answer[j] = -1d;
            } else {
                double temp = prefixSum.get(prefixSum.size()-1+ranges[j][1]) - prefixSum.get(ranges[j][0]);
                answer[j] = temp;
            }
        }
        return answer;
    }
}