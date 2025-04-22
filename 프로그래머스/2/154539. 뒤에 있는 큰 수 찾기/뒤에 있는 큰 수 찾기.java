import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        int N = numbers.length;
        int[] answer = new int[N];
        // -1로 init
        for (int i=0; i<N; i++){
            answer[i]=-1;
        }
        Stack<Integer> stack = new Stack<>();
        stack.add(0);
        for (int i=1; i<N; i++){
            while (!stack.isEmpty() && numbers[stack.peek()] < numbers[i]){
                answer[stack.pop()] = numbers[i];
            }
            stack.add(i);
        }
        return answer;
    }
}
