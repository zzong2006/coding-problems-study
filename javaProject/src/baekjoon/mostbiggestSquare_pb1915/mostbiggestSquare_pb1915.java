package baekjoon.mostbiggestSquare_pb1915;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class mostbiggestSquare_pb1915 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int N, M;
		String [] input = br.readLine().split(" ");
		N = Integer.parseInt(input[0]); 
		M = Integer.parseInt(input[1]); 
		int [][] dp = new int [N + 1][M + 1];
		int [][] map = new int [N + 1][M + 1];
		int maxVal = 0;
		for (int i = 1; i <= N; i++) {
			String inputs = br.readLine();
			for (int j = 1; j <= M; j++) {
				map[i][j] = inputs.charAt(j-1) -'0';
				dp[i][j] = map[i][j];
			}
		}
		
		for (int i = 1; i <= N; i++) {	
			for (int j = 1; j <= M; j++) {
				if(map[i][j] == 1) {
					dp[i][j] = Math.min(Math.min(dp[i][j-1],dp[i-1][j-1]), dp[i-1][j]) + 1; 
					maxVal = Math.max(dp[i][j], maxVal);
				}
				
			}
		}
	
		System.out.println(maxVal * maxVal);
	}
}
