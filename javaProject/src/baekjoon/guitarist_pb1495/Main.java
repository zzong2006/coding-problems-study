package baekjoon.guitarist_pb1495;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
		String[] input = br.readLine().split(" ");
		int n = Integer.parseInt(input[0]);
		int s = Integer.parseInt(input[1]);
		int m = Integer.parseInt(input[2]);
		
		boolean [][] dp = new boolean[n + 1][m + 1];
		dp[0][s] = true;
		
		String[] input2 = br.readLine().split(" ");
		for (int i = 0; i < input2.length; i++) {
			int vol = Integer.parseInt(input2[i]);
			for(int j = 0; j <= m; j ++) {
				if(dp[i][j]) {
					if(j - vol >= 0) {
						dp[i + 1][j - vol] = true; 
					}
					if(j + vol <= m) {
						dp[i + 1][j + vol] = true;
					}
				}
			}
		}
		int max_val = -1;
		for (int j = 0; j<=m; j++) {
			if(dp[n][j]) {
				max_val = Math.max(max_val, j);
			}
		}
		
		bw.write(String.valueOf(max_val));
		bw.flush();
	}
}
