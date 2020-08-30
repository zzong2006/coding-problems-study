// https://programmers.co.kr/learn/courses/30/lessons/60063?language=java
// 블록 이동하기

import java.util.ArrayDeque;
import java.util.Deque;

public class movingBlock {
    public static void main(String[] args) {
        int a = solution(new int[][] {{0, 0, 0, 1, 1},{0, 0, 0, 1, 0},{0, 1, 0, 1, 1},{1, 1, 0, 0, 1},{0, 0, 0, 0, 0}});
        System.out.println(a);
    }
    public static int solution(int[][] board) {
        int N = board.length;
        int [][][][] longPos = new int [N][N][N][N];
        Deque<Machine> mcQue = new ArrayDeque<>();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < N; k++) {
                    for (int l = 0; l < N; l++) {
                        longPos[i][j][k][l] = Integer.MAX_VALUE;
                    }
                }
            }
        }
        // start (0,0) and (0,1)
        Machine mc = new Machine(0,0,0,1);
        longPos[mc.left.y][mc.left.x][mc.right.y][mc.right.y] = mc.tick;
        mcQue.add(mc);
        while(!mcQue.isEmpty()){
            Machine currMC = mcQue.poll();

            // move up down right left

            // rotate
        }

//        int answer = Math.min(longPos[N-1][N-1][N-2][N-1], longPos[][][N-1][N-1]);

        int answer = 0;

        return answer;
    }
}

class Pointer01 {
    public int x;
    public int y;

    public Pointer01(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Machine{
    public Pointer01 left;
    public Pointer01 right;
    public int tick;

    Machine(int x1, int y1, int x2, int y2 ){
        this.left = new Pointer01(x1, y1);
        this.right = new Pointer01(x2, y2);
        this.tick = 0;
    }
}