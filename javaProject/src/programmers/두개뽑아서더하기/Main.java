package programmers.두개뽑아서더하기;

import java.util.Arrays;
import java.util.HashSet;

public class Main {
    public static void main(String[] args) {
        Solution a =  new Solution();
        a.solution(new int[] {2,1,3,4,1});
    }
}

class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = {};
        HashSet<Integer> hs = new HashSet<>();

        for(int i= 0; i< numbers.length; i++){
            for (int j=i + 1; j <numbers.length; j ++){
                hs.add(numbers[i] + numbers[j]);
            }
        }

        int [] s = new int[hs.size()];
        int curr_s = 0;
        for (Object o : hs.toArray()) {
            s[curr_s] = (int) o;
            curr_s += 1;
        }
        Arrays.sort(s);

        return s;
    }
}