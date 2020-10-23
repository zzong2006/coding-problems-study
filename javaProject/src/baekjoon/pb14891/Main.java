package baekjoon.pb14891;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[][] board = new int[4][8];
        for (int i = 0; i < 4; i++) {
            String t = br.readLine();
            for (int j = 0; j < t.length(); j++) {
                board[i][j] = t.charAt(j) -'0';
            }
        }
        int k = Integer.parseInt(br.readLine());
        for (int i = 0; i < k; i++) {
            String[] ip = br.readLine().split(" ");
            int idx = Integer.parseInt(ip[0]) - 1;
            int direction = Integer.parseInt(ip[1]);
            HashSet<Integer> visited = new HashSet<>();
            int[] will_rotate = new int[4];
            Queue<Pair<Integer, Integer>> que = new ArrayDeque<>();
            que.add(new Pair(idx, direction));
            visited.add(idx);
            will_rotate[idx] = direction;

            while(!que.isEmpty()){
                Pair temp = que.poll();
                int temp_idx = (int) temp.x;
                int temp_dir = (int) temp.y;

                if (temp_idx + 1 < 4 && !visited.contains(temp_idx + 1)){
                    if(board[temp_idx][2] != board[temp_idx + 1][6]){
                        que.add(new Pair(temp_idx + 1, temp_dir * -1));
                        will_rotate[temp_idx + 1] = temp_dir * -1;
                        visited.add(temp_idx + 1);
                    }
                }

                if (temp_idx - 1 >= 0 && !visited.contains(temp_idx - 1)){
                    if(board[temp_idx][6] != board[temp_idx - 1][2]){
                        que.add(new Pair(temp_idx - 1, temp_dir * -1));
                        will_rotate[temp_idx - 1] = temp_dir * -1;
                        visited.add(temp_idx - 1);
                    }
                }
            }

            for (int j = 0; j < 4; j++) {
                if (will_rotate[j] != 0) {
                    board[j] = rotate_list(board[j], will_rotate[j]);
                }
            }
        }
        int answer = 0;
        for (int i = 0; i < 4; i++) {
            if (board[i][0] == 1) {
                answer += (Math.pow(2, i));
            }
        }
        System.out.println(answer);

    }

    static int[] rotate_list(int[] ls, int direction) {
        int[] new_ls = new int[ls.length];
        if (direction == -1) {        // 반시계
            new_ls[new_ls.length - 1] = ls[0];
            for (int i = 0; i < new_ls.length - 1; i++) {
                new_ls[i] = ls[i + 1];
            }
        } else {                // 시계
            new_ls[0] = ls[ls.length - 1];
            for (int i = 1; i < new_ls.length; i++) {
                new_ls[i] = ls[i - 1];
            }
        }
        return new_ls;
    }
}
class Pair<X, Y>{
    X x;
    Y y;
    public Pair(X x, Y y ){
        this.x = x;
        this.y = y;
    }
}