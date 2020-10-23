package programmers.EatingShowLive;

import java.util.*;

public class EatingShowLive2 {
    public static void main(String[] args) {
        Solution2 a = new Solution2();
//        a.solution(new int[] {3, 1, 2}, 5);
//        int r = a.solution(new int[] {1}, 3);
        int r = a.solution(new int[] {1,1,1,1}, 4);
        System.out.println("r = " + r);
    }
}

class Solution2 {
    public int solution(int[] food_times, long k) {
        int answer = 0;
        long sum = 0;
        PriorityQueue<Food2> mh = new PriorityQueue<Food2>(
                new Comparator<Food2>() {
                    @Override
                    public int compare(Food2 o1, Food2 o2) {
                        return o1.time - o2.time;
                    }
                }
        );
        // build min-heap
        for (int i = 0; i < food_times.length; i++) {
            int food_time = food_times[i];
            mh.add(new Food2(food_time, i));
        }
        int length = food_times.length;
        // use min-heap
        while(length > 0 && length * (mh.peek().time - sum) <= k){
            Food2 f;
            k -= length * (mh.peek().time - sum);
            do{
                f = mh.poll();
                food_times[f.index] = -1;
                length -= 1;
            } while(!mh.isEmpty() && f.time == mh.peek().time);
            sum = f.time;
        }
        if(length < 1 && k >= 0){                // no food available
            answer = -1;
            return answer;
        }

        long remain = k % (long) (length * (mh.peek().time - sum));
        ArrayList<Food2> remainders = new ArrayList<>();
        while(!mh.isEmpty()){
            remainders.add(mh.poll());
        }

        Collections.sort(remainders, new Comparator<Food2>(){

            @Override
            public int compare(Food2 o1, Food2 o2) {
                return o1.index - o2.index;
            }
        });
        return remainders.get((int)(remain % remainders.size())).index + 1;
    }


}

class Food2 {
    int time;
    int index;

    public Food2(int time, int index) {
        this.time = time;
        this.index = index;
    }
}