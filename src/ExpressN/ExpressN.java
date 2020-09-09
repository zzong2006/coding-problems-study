package ExpressN;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class ExpressN {
    public static void main(String[] args) {
        Solution a = new Solution();
        int k = a.solution(4, 17);
        System.out.println("k = " + k);
    }
}

class Solution {
    public int solution(int N, int number) {
        int [] dp = new int[32001];
        Deque<Integer> que = new ArrayDeque<>();
        Arrays.fill(dp, Integer.MAX_VALUE);

        dp[N]  = 1;
        dp[N * 11]  = 2;
        dp[N * 111]  = 3;
        dp[N * 1111]  = 4;
        boolean changed = true;
        que.add(N); que.add(N * 11); que.add(N * 111); que.add(N * 1111);

        while(!que.isEmpty()){
            int val = que.poll();
            // minus
            int curr = val - N;
            int count = dp[val];
            while(curr > 0 && count <= 9){
                if(dp[curr] > count + 1){
                    dp[curr] = count + 1;
                    que.add(curr);
                }
                count = dp[curr];
                curr -= N;
            }

            // plus
            curr = val + N;
            count = dp[val];
            while(curr < dp.length && count <= 9){
                if(dp[curr] > count + 1){
                    dp[curr] = count + 1;
                    que.add(curr);
                }
                count = dp[curr];
                curr += N;
            }

            // multiply
            curr = val * N;
            count = dp[val];
            while(curr < dp.length && count <= 9){
                if(dp[curr] > count + 1){
                    dp[curr] = count + 1;
                    que.add(curr);
                }
                count = dp[curr];
                curr *= N;
            }

            // division
            curr = val / N;
            count = dp[val];
            while(curr > 0 && count <= 9){
                if(dp[curr] > count + 1){
                    dp[curr] = count + 1;
                    que.add(curr);
                }
                count = dp[curr];
                curr /= N;
            }
        }
        if(dp[number] > 8)
            return -1;
        else{
            return dp[number];
        }
    }
}