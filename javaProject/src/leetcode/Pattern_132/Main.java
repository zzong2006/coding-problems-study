package leetcode.Pattern_132;

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) {
        Solution a = new Solution();
        boolean result = a.find132pattern(new int[]{1,-4,2,-1});
        System.out.println("result = " + result);
    }
}

class Solution {
    public boolean find132pattern(int[] nums) {
        int[] min_i = new int[nums.length];
        min_i[0] = nums[0];
        for (int j = 1; j < nums.length - 1; j++) {
            min_i[j] = Math.min(min_i[j - 1], nums[j]);
            if(min_i[j] < nums[j]){
                for (int k = j + 1; k < nums.length; k++) {
                    if(min_i[j] < nums[k] && nums[k] < nums[j]){
                        return true;
                    }
                }
            }
        }
        return false;
    }
}