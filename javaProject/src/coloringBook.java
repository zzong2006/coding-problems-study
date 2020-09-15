// https://programmers.co.kr/learn/courses/30/lessons/1829 
// 카카오프렌즈 컬러링북
// Note : Long 데이터 형식이 함정임
import java.util.ArrayDeque;
import java.util.Deque;

public class coloringBook {
    public static int [][] move = {{0,1},{-1,0},{1,0},{0,-1}};
    public static void main(String[] args) {
        int [] a = solution(6, 4 , new int [][] {
                {0, 1, 1, 1},
                {1, 2, 2, 1},
                {2, 2, 2, 1},
                {0, 0, 2, 1},
                {0, 3, 0, 3},
                {0, 0, 3, 3}});
        for (int i = 0; i < a.length; i++) {
            System.out.print(a[i] + " ");
        }
        System.out.println();

        int [] b = solution(13, 16 , new int [][] {
                {0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0},
                {0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0},
                {0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0},
                {0, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0},
                {0, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 0},
                {0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0},
                {0, 1, 3, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 3, 1, 0},
                {0, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 0},
                {0, 0, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 0, 0},
                {0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0},
                {0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0}});
        for (int i = 0; i < b.length; i++) {
            System.out.print(b[i] + " ");
        }
        System.out.println();
    }

    public static int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        long [][] realPicture = new long[m][n];
        int[] answer = new int[2];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                realPicture[i][j] = picture[i][j];
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if(realPicture[i][j] != 0){
                    long curr = realPicture[i][j];
                    realPicture[i][j] = 0;
                    int area = dfs(m, n, realPicture, curr, new Pointer(j,i));
                    maxSizeOfOneArea = Math.max(area, maxSizeOfOneArea);
                    numberOfArea += 1;
                }
            }
        }
        
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }

    public static int dfs(int m, int n, long[][] board, long num, Pointer start){
        Deque<Pointer> bag = new ArrayDeque<>();
        bag.add(start);
        int area = 1;
        while(!bag.isEmpty()){
            Pointer a = bag.poll();
            for (int i = 0; i < move.length; i++) {
                if(a.x + move[i][0] < n && a.x + move[i][0] >= 0 &&
                    a.y + move[i][1] < m && a.y + move[i][1] >= 0 &&
                    board[a.y + move[i][1]][a.x + move[i][0]] == num){
                    board[a.y + move[i][1]][a.x + move[i][0]] = 0;
                    bag.add(new Pointer(a.x + move[i][0] , a.y + move[i][1]));
                    area += 1;
                }
            }
        }
        return area;
    }
}

class Pointer {
    public Pointer(int x, int y) {
        super();
        this.x = x;
        this.y = y;
    }
    public Pointer() {
        this.x = 0;
        this.y = 0;
    }
    public int x;
    public int y;

    public void setPointer(Pointer A) {
        this.x = A.x;
        this.y = A.y;
    }

    public boolean equals(Pointer A) {
        if( this.x == A.x && this.y ==A.y )
            return true;
        else
            return false;
    }
}