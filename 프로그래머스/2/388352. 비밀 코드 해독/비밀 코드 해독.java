import java.util.*;

class Solution {
    static ArrayList<ArrayList<String>> tempAnswer;
    static ArrayList<String> numList;
    static int answer = 0;
    
    public int solution(int n, int[][] q, int[] ans) {
        int answer = 0;
        // 1부터 n이 담긴 배열에서, 1부터 n개 뽑기
        numList = new ArrayList<>();
        for (int i=1; i<=n; i++){
            numList.add(String.valueOf(i));
        }
        //combination을 반환시킨다.
        for (int i=5; i<=5; i++){
            ArrayList<ArrayList<String>> list = combination(i);
            //q와 ans를 사용해서, 만족하는 조합을 받아내자!
            for (int k=0; k<list.size(); k++){
                ArrayList<String> tempList = list.get(k);
                boolean flag = true;
                for (int j=0; j<q.length; j++){
                    //한 번이라도 틀리면 flag = False
                    int count = countNum(q[j], tempList);
                    if (count != ans[j]){
                        flag = false;
                    }
                }
                if (flag==true){
                    // System.out.println(tempList);
                    answer += 1;
                }
            }
        }
        
        return answer;
    }
    
    public static ArrayList<ArrayList<String>> combination(int N){ //N개의 원소를 뽑는다.
        tempAnswer = new ArrayList<ArrayList<String>>();
        combine(0, new ArrayList<String>(), N);
        return tempAnswer;
    }
    
    public static void combine(int start, ArrayList<String> list, int size){
        if (list.size() == size){
            tempAnswer.add(new ArrayList(list));
            return;
        }
        for (int i=start; i<numList.size(); i++){
            list.add(numList.get(i));
            combine(i+1, list, size);
            list.remove(list.size()-1);
        }       
    }
    
    public static int countNum(int[] array, ArrayList<String> list){
        int count = 0;
        for (int i=0; i<array.length; i++){
            for (int j=0; j<list.size(); j++){
                if (array[i] == Integer.parseInt(list.get(j))){
                    count += 1;
                }
            }
        }
        return count;
    }
}