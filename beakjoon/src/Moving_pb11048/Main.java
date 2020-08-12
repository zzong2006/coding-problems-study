package Moving_pb11048;


import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String [] inp = br.readLine().split(" ");
		int n = Integer.parseInt(inp[0]);
		int m = Integer.parseInt(inp[1]);
		
		int [][] map = new int [n + 1][m + 1];
		int [][] dp = new int [n + 1][m + 1];

		
		for (int i = 1; i <= n; i++) {
			String [] input = br.readLine().split(" ");
			for (int j = 1; j <= m; j++) {
				map[i][j] = Integer.parseInt(input[j-1]);
			}
		}
		
		int max_val = 0;
		
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				if(i == 1) {
					dp[i][j] = dp[i][j-1] + map[i][j];
				} else {
					if(j == 1) {
						dp[i][j] = dp[i-1][j] + map[i][j];
					} else {
						dp[i][j] = dp[i-1][j-1] + map[i][j];
						dp[i][j] = Math.max(dp[i-1][j] + map[i][j], dp[i][j] );
						dp[i][j] = Math.max(dp[i][j-1] + map[i][j], dp[i][j] );
					}
				}
				max_val = Math.max(max_val, dp[i][j]);
			}
		}
		System.out.println(max_val);
	}
}

