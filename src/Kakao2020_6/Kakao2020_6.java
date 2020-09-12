package Kakao2020_6;

import java.util.*;

public class Kakao2020_6 {
    public static void main(String[] args) {
        Solution a = new Solution();
        Queue<Integer> ax = new ArrayDeque<Integer>();
        System.out.println("[[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]".replaceAll("\\[", "{")
        .replaceAll("\\]", "}"));
        int res;

        res = a.solution(new int[][] {{1,0,0,3},{2,0,0,0},{0,0,0,2},{3,0,1,0}}, 1, 0);
        System.out.println("res = " + res);

        res = a.solution(new int[][] {{3,0,0,2},{0,0,1,0},{0,1,0,0},{2,0,0,3}}, 1, 0);
        System.out.println("res = " + res);

    }
}

class Solution {
    static ArrayList<Integer> [] perms = new ArrayList[25];
    static int curr = 0;
    static int maxVal = -1;
    public int solution(int[][] board, int r, int c) {
        int answer = 0;
        ArrayList<Integer> ls = new ArrayList<Integer>();

        for (int[] ints : board) {
            for (int a : ints) {
                maxVal = Math.max(a, maxVal);
            }
        }
        for (int i = 0; i < maxVal; i++) {
            ls.add(i + 1);
        }
        permute(ls, 0);

        return answer;
    }

    public static void doSomething(ArrayList<Integer> a, int card, int i, int j){

    }

    static void permute(ArrayList<Integer> arr, int k){
        for(int i = k; i < arr.size(); i++){
            Collections.swap(arr, i, k);
            permute(arr, k+1);
            Collections.swap(arr, k, i);
        }
        if (k == arr.size() -1){
            ArrayList <Integer> temp = new ArrayList<>();
            for (int i = 0; i < maxVal; i++) {
                temp.add(arr.get(i));
            }
            perms[curr]= temp;
            curr += 1;
        }
    }
}