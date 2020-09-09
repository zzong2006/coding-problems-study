package HIndex;

import java.util.Arrays;

public class HIndex {
    public static void main(String[] args) {
        Solution a = new Solution();
        int k = a.solution(new int[] {20,21,22,23});
        System.out.println("k = " + k);
    }
}

class Solution {
    public int solution(int[] citations) {
        int answer = -1;
        int [] index = new int[citations.length];
        
        Arrays.sort(citations);
        // 0, 1, 4, 4, 4
        // 0, 1, 3, 5, 6
        int curr = citations[citations.length - 1];
        int last = citations[0];
//        if(last > citations.length || curr < citations.length){
//            answer = citations.length;
//            return answer;
//        }
        for (int i = citations.length - 1 ; i >= 0; i--) {
            if(i != 0){
                do {
                    if(curr == (citations.length - i)){
                        answer = curr;
                        break;
                    } else {
                        if(curr > citations[i - 1]){
                            curr -= 1;
                        } else{
                            break;
                        }
                    }
                } while(true);
            } else {
                while(true){
                    if(curr == citations.length){
                        answer = curr;
                        break;
                    } else{
                        if(curr != 0)
                            curr -= 1;
                        else{
                            answer = curr;
                            break;
                        }
                    }
                }
            }
            if(answer != -1)
                break;
        }
        return answer;
    }
}