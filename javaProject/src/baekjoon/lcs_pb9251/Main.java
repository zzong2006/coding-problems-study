package baekjoon.lcs_pb9251;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String a = br.readLine();
		String b = br.readLine();
		int a_len = a.length();
		int b_len = b.length();
		
		int [][] dp = new int [a_len + 1][b_len + 1];
		int max_val = 0;
		
		for (int i = 1; i <= a_len; i++) {
			for (int j = 1; j <= b_len; j++) {
				dp[i][j] = Math.max(dp[i - 1][j - 1] , dp[i - 1][j]);
				dp[i][j] = Math.max(dp[i][j], dp[i][j - 1]);
				
				if(a.charAt(i - 1) == b.charAt(j - 1)){
					if(dp[i][j] + 1 <= j && dp[i][j] + 1 <= i ) {
						dp[i][j] = Math.max(dp[i - 1][j - 1] + 1 , dp[i - 1][j]);
						max_val = Math.max(dp[i][j], max_val);
					}
				} 
			}
		}
		
		bw.write(String.valueOf(max_val));
		bw.flush();
	}
}
