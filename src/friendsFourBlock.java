import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class friendsFourBlock {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Solution a = new Solution();

        bw.write(a.solution(4, 5, new String [] {"CCBDE", "AAADE", "AAABF", "CCBBF"}) + "\n");
        bw.write(a.solution(6, 6, new String [] {"TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"}) + "\n");
        bw.write(a.solution(4, 4, new String [] {"ZZZZ", "ZAAZ","ZAAZ","ZZZZ"}) + "\n");
        bw.write(a.solution(2, 3, new String [] {"QWA", "ZXC"}) + "\n");
        bw.write(a.solution(3, 2, new String [] {"AA", "AA", "AB"}) + "\n");
        bw.write(a.solution(4, 2, new String [] {"CC", "AA", "AA","CC"}) + "\n");
        bw.write(a.solution(6, 2, new String [] {"DD", "CC", "AA", "AA", "CC", "DD"}) + "\n");
        bw.write(a.solution(8, 2, new String [] {"FF", "AA", "CC", "AA", "AA", "CC","DD","FF"}) + "\n");
        bw.write(a.solution(6, 2, new String [] {"AA", "AA", "CC", "AA", "AA", "DD"}) + "\n");
        bw.flush();
    }
    static class Solution {

        public int solution(int m, int n, String[] board) {
            int answer = 0;
            StringBuilder [] boardBuilder = new StringBuilder[m];
            for (int i = 0; i < m; i++) {
                boardBuilder[i] = new StringBuilder(board[i]);
            }
            int count ;
            do {
                count = search(m, n, boardBuilder);
                if(count > 0){
                    searchForMoveDown(m, n, boardBuilder);
                    answer += count;
                }
            } while(count > 0);

            return answer;
        }

        public int search(int m, int n, StringBuilder[] board){
            int count = 0;
            for (int i = 0; i < m - 1; i++) {
                for (int j = 0; j < n - 1; j++) {
                    if(isSquare(i, j, board)){
                        count += change(i, j, board);
                    }
                }
            }
            return count;
        }

        public void searchForMoveDown(int m, int n, StringBuilder[] board){
            for (int i = m - 1; i >= 0; i--) {
                for (int j = n - 1; j >= 0; j--) {
                    if( (board[i].charAt(j) >= 97 && board[i].charAt(j) <= 122) || board[i].charAt(j) == '0'){
                        if(!moveDown(i, j, m, board)){
                            board[i].setCharAt(j, '0');
                        }
                    }
                }
            }
        }

        public boolean isSquare(int i, int j,  StringBuilder[] board){
            char f = board[i].charAt(j);
            if (f == '0')
                return false;
            // to Upper Case
            if(!(65 <= f && 90 >= f))
                f -= 32;
            int [][] dir = {{1, 1}, {1, 0}, {0, 1}};

            if( (board[i + 1].charAt(j + 1) == f || board[i + 1].charAt(j + 1) == f + 32)
            && (board[i + 1].charAt(j) == f || board[i + 1].charAt(j) == f + 32)
            && (board[i].charAt(j + 1) == f || board[i].charAt(j + 1) == f + 32) )
                return true;
            else
                return false;
        }

        public int change(int i, int j, StringBuilder[] board){
            char f = board[i].charAt(j);
            if(!(65 <= f && 90 >= f))
                f -= 32;
            int [][] dir = {{1, 1}, {1, 0}, {0, 1}, {0, 0}};
            int count = 0;

            for (int k = 0; k < dir.length; k++) {
                if(board[i + dir[k][0]].charAt(j + dir[k][1]) == f) {
                    count += 1;
                    board[i + dir[k][0]].setCharAt(j + dir[k][1], (char)(f + 32));
                }
            }

            return count;
        }

        // if any changed happened then return true or return false.
        public boolean moveDown(int i, int j, int m, StringBuilder [] board){
            boolean changed = false;
            int originalI = i;
            i -= 1;
            while(i >= 0){
                if(65 <= board[i].charAt(j) && 90 >= board[i].charAt(j)){
                    board[originalI].setCharAt(j, board[i].charAt(j));
                    board[i].setCharAt(j, '0');
                    changed = true;
                    break;
                }
                i -= 1;
            }
            return changed;
        }
    }
}
