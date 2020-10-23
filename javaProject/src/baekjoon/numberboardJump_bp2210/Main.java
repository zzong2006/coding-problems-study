package baekjoon.numberboardJump_bp2210;


import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashSet;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		// String [] inp = br.readLine().split(" ");
		int n = 5;
		
		String [][] map = new String [5][5];
		HashSet<String> ans = new HashSet<String>();
		
		for (int i = 0; i < n; i++) {
			String [] input = br.readLine().split(" ");
			for (int j = 0; j < n; j++) {
				map[i][j] = input[j];
			}
		}
		
		int max_val = 0;
		
		for (int i = 0; i < n; i++) {
			
			for (int j = 0; j < n; j++) {
				movingBoard(map, "",i, j, ans);
			} 
		}
		
		System.out.println(ans.size());
		
	}
	
	public static void movingBoard(String[][] map, String curr, int x, int y, HashSet<String> st) {
		curr = curr.concat(map[x][y]);
		
		if(curr.length() == 6) {
			st.add(curr);
			return ;
		} else {
			if( x + 1 < 5) {
				movingBoard(map, curr, x + 1 ,y , st);
			}
			if( y + 1 < 5) {
				movingBoard(map, curr, x,y + 1 , st);
			}
			if( y - 1 >= 0) {
				movingBoard(map, curr, x,y - 1 , st);
			}
			if( x - 1 >= 0) {
				movingBoard(map, curr, x - 1,y , st);
			}
		}
	}
}

