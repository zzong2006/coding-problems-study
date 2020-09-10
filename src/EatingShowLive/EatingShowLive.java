package EatingShowLive;


import java.util.*;

public class EatingShowLive {
    public static void main(String[] args) {
        Solution2 a = new Solution2();
//        a.solution(new int[] {3, 1, 2}, 5);
//        int r = a.solution(new int[] {1}, 3);
        int r = a.solution(new int[] {1,1,1,1}, 4);
        System.out.println("r = " + r);
    }
}


class Solution {
    public int solution(int[] food_times, long k) {
        int answer = 0;
        long sum = 0;
        MinHeap mh = new MinHeap(food_times.length, 1);

        // build min-heap
        for (int i = 0; i < food_times.length; i++) {
            int food_time = food_times[i];
            mh.insert(food_time, i);
        }
        int length = food_times.length;
        // use min-heap
        while(length * (mh.getRoot().time - sum)  <= k && length > 0){
            Food2 f;
            k -= length * (mh.getRoot().time - sum);
            do{
                f = mh.getRoot();
                food_times[f.index] = -1;
                mh.pop();
                length -= 1;
            } while(f.time == mh.getRoot().time && mh.curr != 1);
            sum = f.time;
        }
        if(length < 1 && k >= 0){                // no food available
            answer = -1;
            return answer;
        }

        long remain = k % (long) (length * (mh.getRoot().time - sum));
        ArrayList<Food2> remainders = new ArrayList<>();
        for (int i = 1; i < mh.curr; i++) {
            remainders.add(mh.content[i]);
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
class MinHeap{
    Food2[] content ;
    int curr;

    public MinHeap(int length, int curr) {
        this.content = new Food2[length + 1];
        this.curr = curr;
    }

    public void insert(int i, int idx){
        if(curr == 1){
            content[curr] = new Food2(i, idx);
        } else {
            content[curr] = new Food2(i, idx);
            int childCurr = curr;
            while(childCurr > 1){
                if(content[childCurr / 2].time <= content[childCurr].time){
                    break;
                } else{     // swap
                    Food2 temp = content[childCurr / 2];
                    content[childCurr / 2] = content[childCurr];
                    content[childCurr] = temp;
                    childCurr /= 2;
                }
            }
        }
        curr += 1;
    }

    public void pop(){      // remove root
        curr -= 1;
        content[1] = content[curr];
        int headIdx = 1;
        while(headIdx < curr){
            if(headIdx * 2 + 1 < curr){     // have both children
                int swapIdx = -1;
                if(content[headIdx * 2].time < content[headIdx].time && content[headIdx * 2 + 1].time < content[headIdx].time){
                    if(content[headIdx * 2].time <= content[headIdx * 2 + 1].time){
                        swapIdx = headIdx * 2;
                    } else {
                        swapIdx = headIdx * 2 + 1;
                    }
                } else if(content[headIdx * 2].time >= content[headIdx].time && content[headIdx * 2 + 1].time < content[headIdx].time) {
                    swapIdx = headIdx * 2 + 1;
                } else if(content[headIdx * 2].time < content[headIdx].time && content[headIdx * 2 + 1].time >= content[headIdx].time){
                    swapIdx = headIdx * 2;
                } else {
                    break;
                }
                Food2 temp = content[swapIdx];
                content[swapIdx] = content[headIdx];
                content[headIdx] = temp;
                headIdx = swapIdx;
            } else if(headIdx * 2 + 1 == curr) {        // have only one child
                if(content[headIdx * 2].time < content[headIdx].time){
                    Food2 temp = content[headIdx * 2];
                    content[headIdx * 2] = content[headIdx];
                    content[headIdx] = temp;
                }
                headIdx *= 2;
            } else {            // no children
               break;
            }
        }
    }

    public Food2 getRoot(){
        return content[1];
    }
}

class Food{
    int time;
    int index;

    public Food(int time, int index) {
        this.time = time;
        this.index = index;
    }
}