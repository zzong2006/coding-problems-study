package Practice;

import java.util.*;

public class Practice {
    static Deque<int[]> combs = new LinkedList<>();

    public static void main(String[] args) {
        // Deque 사용법
        Deque<Integer> a = new ArrayDeque<>();
        for (int i = 0; i < 10; i++) {
            a.add(i);
        }
        System.out.println("a.pollFirst() = " + a.pollFirst());
        System.out.println("a.pollLast() = " + a.pollLast());
        for (Iterator<Integer> it = a.iterator(); it.hasNext(); ) {
            Integer next = it.next();
            System.out.print(next + " ");
        }
        System.out.println();

        // Combinations (직접 구현해야됨)
        combinations(new int[] {1,2,3,4}, 0, 3, 0, new int [] {});

        for (int[] comb : combs) {
            for (int i = 0; i < comb.length; i++) {
                System.out.print(comb[i] + " ");
            }
            System.out.println();
        }

        // Permutations (직접 구현해야됨)


    }

    static void combinations(int[] array, int curr, int k, int o, int[] ls) {
        if(o == k){
            combs.add(ls);
        } else{
            for (int i = curr; i < array.length; i++) {
                int [] new_ls = new int[k];
                for (int j = 0; j < ls.length; j++) {
                    new_ls[j] = ls[j];
                }
                new_ls[o] = array[i];
                combinations(array, i + 1, k, o + 1, new_ls);
            }
        }

    }

}

class Solution {
    public int[] solution(int[][] v) {
        int[] answer = {};


        return answer;
    }
}