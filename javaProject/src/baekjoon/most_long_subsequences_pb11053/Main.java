package baekjoon.most_long_subsequences_pb11053;


import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		int [] dp = new int [1101];
		String [] input = br.readLine().split(" ");
		int [] nums = new int [n];

		for (int i = 0; i < n; i++) {
			nums[i] = Integer.parseInt(input[i]);
		}

		int max_count = 0;
		for(int i=0; i<1021; i++) {
			dp[i] = 1;
		}
		
		for (int i = 1; i < n; i++) {
			boolean check = false;
			for (int j = 0; j < i; j++) {
				if(nums[i] > nums[j] ) {
					dp[i] = Math.max(dp[i], dp[j] + 1);
				}
			}

		}
		
		for(int i=1; i<1021; i++) {
			max_count = Math.max(max_count, dp[i]);
		}
		bw.write(String.valueOf(max_count));
		bw.flush();
	}
}

