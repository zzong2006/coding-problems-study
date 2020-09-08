package BlockGame;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Queue;

public class BlockGame {
    public static void main(String[] args) {
        System.out.println("[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]".replaceAll("\\[","\\{").replaceAll("\\]","\\}"));
        Solution a = new Solution();
        int output = a.solution(new int[][] {
                {0,0,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,4,0,0,0},
                {0,0,0,0,0,4,4,0,0,0},
                {0,0,0,0,3,0,4,0,0,0},
                {0,0,0,2,3,0,0,0,5,5},
                {1,2,2,2,3,3,0,0,0,5},
                {1,1,1,0,0,0,0,0,0,5}}
        );
        System.out.println(output);
    }
}

class Solution {
    public int solution(int[][] board) {
        int answer = 0;
        int[][][] lowBlock = { {{1,0,0},{1,1,1}}, {{0,0,1},{1,1,1}},{{0,1,0},{1,1,1}} };
        int[][][] highBlock = {{{0,1},{0,1},{1,1}}, {{1,0},{1,0},{1,1}}};
        Deque<Strategy> que = new ArrayDeque<>();
        que.add(new Strategy(board, 0));

        while(!que.isEmpty()){
            Strategy a = que.poll();
            answer = Math.max(a.count, answer);
            int[][] tempBoard = a.board;
            /* search block (with type) */
            // search low Block
            for (int i = 0; i < tempBoard.length - 1; i++) {
                for (int j = 0; j < tempBoard[0].length - 2; j++) {
                    if(tempBoard[i + 1][j] != 0 && tempBoard[i + 1][j + 1] != 0 && tempBoard[i + 1][j + 2] != 0){       // 바닥이 있는 블록 ㅗ, ㄴ 등
                        // do matching
                        int tempInt = tempBoard[i + 1][j];
                        for (int k = 0; k < lowBlock.length; k++) {
                            boolean theBlock = true;
                            for (int l = 0; l < lowBlock[k].length; l++) {
                                for (int m = 0; m < lowBlock[k][0].length; m++) {
                                    if(lowBlock[k][l][m] != 0 ){
                                        theBlock &= (tempBoard[i + l][j + m] == tempInt);
                                    }
                                }
                            }
                            // 블록 확인되었을 경우 직사각형 만들 수 있는지 체크 (빈 공간 위에 아무것도 없어야함)
                            if(theBlock){
                                boolean makeSquare = true;
                                if(k == 0){
                                    for (int l = i; l >= 0; l--) {
                                        for (int m = j + 1; m < j + 3; m++) {
                                            if(tempBoard[l][m] != 0){
                                                makeSquare = false;
                                                break;
                                            }
                                        }
                                        if(!makeSquare)
                                            break;
                                    }
                                } else if(k == 1){
                                    for (int l = i; l >= 0; l--) {
                                        for (int m = j ; m < j + 2; m++) {
                                            if(tempBoard[l][m] != 0){
                                                makeSquare = false;
                                                break;
                                            }
                                        }
                                        if(!makeSquare)
                                            break;
                                    }
                                } else if(k == 2){
                                    for (int l = i; l >= 0; l--) {
                                        if(tempBoard[l][j] != 0 || tempBoard[l][j + 2] != 0){
                                            makeSquare = false;
                                            break;
                                        }
                                    }
                                }
                                // 만들 수 있으면 해당 부분 지우고, count 하나 올리고, board를 queue에 넣음
                                if(makeSquare){
                                    Strategy another = new Strategy(tempBoard, a.count + 1);
                                    if(k == 0){
                                        another.board[i][j] = 0; another.board[i + 1][j] = 0;
                                        another.board[i + 1][j + 1] = 0; another.board[i + 1][j + 2] = 0;
                                    } else if(k == 1){
                                        another.board[i][j + 2] = 0; another.board[i + 1][j] = 0;
                                        another.board[i + 1][j + 1] = 0; another.board[i + 1][j + 2] = 0;
                                    } else {
                                        another.board[i][j + 1] = 0; another.board[i + 1][j] = 0;
                                        another.board[i + 1][j + 1] = 0; another.board[i + 1][j + 2] = 0;
                                    }
                                    que.add(another);
                                }
                            }
                        }
                    }
                }
            }

            // int[][][] highBlock = {{{0,1},{0,1},{1,1}}, {{1,0},{1,0},{1,1}}};
            // search high Block
            for (int i = 0; i < tempBoard.length - 2; i++) {
                for (int j = 0; j < tempBoard[0].length - 1; j++) {
                    if(tempBoard[i + 2][j] != 0 && tempBoard[i + 2][j + 1] != 0) {       // 바닥이 있는 블록
                        // do matching
                        int tempInt = tempBoard[i + 2][j];
                        for (int k = 0; k < highBlock.length; k++) {
                            boolean theBlock = true;
                            for (int l = 0; l < highBlock[k].length; l++) {
                                for (int m = 0; m < highBlock[k][0].length; m++) {
                                    if(highBlock[k][l][m] != 0 ){
                                        theBlock &= (tempBoard[i + l][j + m] == tempInt);
                                    }
                                }
                            }
                            // 블록 확인되었을 경우 직사각형 만들 수 있는지 체크 (빈 공간 위에 아무것도 없어야함)
                            if(theBlock){
                                boolean makeSquare = true;
                                if(k == 0){
                                    for (int l = i+1; l >= 0; l--) {
                                        if(tempBoard[l][j] != 0){
                                            makeSquare = false;
                                            break;
                                        }
                                    }
                                } else if(k == 1){
                                    for (int l = i+1; l >= 0; l--) {
                                        if(tempBoard[l][j+1] != 0){
                                            makeSquare = false;
                                            break;
                                        }
                                    }
                                }

                                // 만들 수 있으면 해당 부분 지우고, count 하나 올리고, board를 queue에 넣음
                                if(makeSquare){
                                    Strategy another = new Strategy(tempBoard, a.count + 1);
                                    if(k == 0){
                                        another.board[i][j + 1] = 0; another.board[i + 2][j] = 0;
                                        another.board[i + 1][j + 1] = 0; another.board[i + 2][j + 1] = 0;
                                    } else if(k == 1){
                                        another.board[i][j] = 0; another.board[i + 2][j] = 0;
                                        another.board[i + 1][j] = 0; another.board[i + 2][j + 1] = 0;
                                    }
                                    que.add(another);
                                }
                            }
                        }
                    }
                }
            }
        }


        return answer;
    }

}

class Strategy {
    public int [][] board;
    public int count ;
    Strategy(int [][] a, int count){
        this.board = new int[a.length][a[0].length];
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[0].length; j++) {
                this.board[i][j] = a[i][j];
            }
        }
        this.count = count;
    }
}

class Block {
    public int x;
    public int y;
    public int type;

    Block(int x, int y, int type) {
        this.x = x;
        this.y = y;
        this.type = type;
    }
}

