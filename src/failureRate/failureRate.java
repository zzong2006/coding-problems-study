package failureRate;

import java.util.Arrays;
import java.util.Collections;

public class failureRate {
    public static void main(String[] args) {
        Solution a = new Solution();
        int [] s = a.solution(5, new int[] {2, 1, 2, 6, 2, 4, 3, 3}) ;
        for (int q: s) {
            System.out.print(q + " ");
        }
        System.out.println();
        s = a.solution(4, new int[] {4, 4, 4, 4}) ;
        for (int q: s) {
            System.out.print(q + " ");
        }
    }
}

class Solution {
    public int[] solution(int N, int[] stages) {
        int[] clear = new int [N + 2];
        int[] notClear = new int [N + 2];

        int[] answer = new int [N];

        for (int i = 0; i < stages.length; i++) {
            int stage = stages[i];
            for (int j = 1; j <= stage; j++) {
                clear[j] += 1;
            }
            notClear[stage] += 1;
        }
        ffrr[] fr = new ffrr [N];

        for (int i = 1; i <= N; i++) {
            if(clear[i] == 0)
                fr[i - 1] = new ffrr(0, i);
            else
                fr[i - 1] = new ffrr((double) notClear[i]/ (double) clear[i], i);
        }
        try {
            Arrays.sort(fr);
        } catch (Exception e){
            e.printStackTrace();
        }

        for (int i = 0; i < N; i++) {
            answer[i ] = fr[i].stageNum;
        }
        return answer;
    }
}

class ffrr implements Comparable{
    public double val;
    public int stageNum;

    public ffrr(double val, int num){
        this.val = val;
        this.stageNum = num;
    }

    @Override
    public int compareTo(Object o) {
        ffrr temp = (ffrr) o;
        if(this.val - temp.val == 0){
            if(this.stageNum > temp.stageNum){
                return 1;
            } else {
                return -1;
            }
        } else if(this.val > temp.val) {
            return -1;
        } else {
            return 1;
        }
    }
}