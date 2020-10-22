package Asteroid_Collision;

import java.util.Stack;

import static java.lang.Math.abs;

class Main {
    public static void main(String[] args) {
        Solution a = new Solution();
        a.asteroidCollision(new int[]{-2, 2, 1, -2});
    }
}

class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> s = new Stack<>();

        for (int i = 0; i < asteroids.length; i++) {
            if (s.isEmpty()) {
                s.add(asteroids[i]);
            } else {
                int le = s.lastElement();
                int input = asteroids[i];
                if (le < 0 && input > 0) {
                    s.add(input);
                } else if (le > 0 && input < 0) {
                    if (le > abs(input)) {
                        // do nothing (input asteroid is exploded)
                    } else if (le == abs(input)) {
                        s.pop();
                    } else {     // le < input
                        while (!s.isEmpty() && le < abs(input) && (le > 0)) {
                            s.pop();
                            if (!s.isEmpty()) {
                                le = s.lastElement();
                            }
                        }
                        if (s.isEmpty()) {
                            s.add(input);
                        } else if (le < 0) {
                            s.add(input);
                        } else if (le > abs(input)) {
                            // do nothing
                        } else if (le == abs(input)){
                            s.pop();
                        }
                    }
                } else {
                    s.add(input);
                }
            }
        }
        System.out.println("s = " + s);

        int[] ans = new int[s.size()];
        for (int i = s.size() - 1; i >= 0; i--) {
            ans[i] = s.pop();
        }
        return ans;
    }
}