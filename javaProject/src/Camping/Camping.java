package Camping;

import java.util.Arrays;

public class Camping {
    public static void main(String[] args) {
        Solution a = new Solution();
        int s = a.solution(4, new int[][] {{0, 0}, {0, (int)(Math.pow(2,31)-1)}, {0, 2}, {2, 0}, {2, 2}});
        System.out.println(s);
    }
}


class Solution {
    public int solution(int n, int[][] data) {
        int answer = 0;
        for (int i = 0; i < data.length; i++) {
            for (int j = i + 1; j < data.length; j++) {
                if(i != j && area(data[i], data[j])  && inner(data, data[i], data[j])){
                    answer += 1;
                    System.out.println(data[i][0] + " " + data[i][1] + " / " + data[j][0] + " " + data[j][1]);
                }
            }
        }
        // Arrays.sort();

        return answer;
    }

    public boolean inner(int[][] data, int [] a, int [] b){
        int higherX = Math.max(a[0],b[0]);
        int lowerX = Math.min(a[0],b[0]);
        int higherY = Math.max(a[1],b[1]);
        int lowerY = Math.min(a[1],b[1]);

        for (int i = 0; i < data.length; i++) {
            if(lowerX < data[i][0] && data[i][0] < higherX && data[i][1] < higherY && data[i][1] > lowerY)
                return false;
        }
        return true;
    }
    public boolean area(int [] a, int [] b){
        return ((a[0] != b[0]) && (a[1] != b[1]));
    }
}