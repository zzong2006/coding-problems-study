package leetcode.Minimum_Dept_of_Binary_Tree;

import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) {

    }
}

class Solution {
    public int minDepth(TreeNode root) {
        if (root != null){
            int answer = Integer.MAX_VALUE;
            PriorityQueue<Pair<TreeNode, Integer>> que = new PriorityQueue<>(new Comparator<Pair<TreeNode, Integer>>() {
                @Override
                public int compare(Pair<TreeNode, Integer> o1, Pair<TreeNode, Integer> o2) {
                    return o1.y - o2.y;
                }
            });

            que.add(new Pair<>(root, 1));
            while (!que.isEmpty()) {
                Pair t = que.poll();
                TreeNode curr_tree = (TreeNode) t.x;
                int count = (int) t.y;
                if (curr_tree.left == null && curr_tree.right == null){
                    answer = Math.min(answer, count);
                    return answer;
                } else{
                    if (curr_tree.left != null){
                        que.add(new Pair<>(curr_tree.left, count + 1));
                    }
                    if (curr_tree.right != null){
                        que.add(new Pair<>(curr_tree.right, count + 1));
                    }
                }
            }
            return answer;
        } else{
            return 0;
        }
    }
}

class Pair<X, Y> {
    public final X x;
    public final Y y;

    public Pair(X x, Y y) {
        this.x = x;
        this.y = y;
    }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}