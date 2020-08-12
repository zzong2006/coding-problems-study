package lcs2_pb9252;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class lcs2_pb9252 {
	static int [] parents ;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String a = br.readLine();
		String b = br.readLine();
		int aLen = a.length();
		int bLen = b.length();
		int [][] dp = new int [aLen + 1][bLen + 1];
		
		//find the longest length of LCS
		
		for (int i = 1; i <= aLen; i++) {
			for (int j = 1; j <= bLen; j++) {
				if(a.charAt(i-1) == b.charAt(j-1)) {
					dp[i][j] = dp[i-1][j-1] + 1;
				} else {
					dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
				}
			}
		}
		
		// find LCS
		String LCS = "";
		int searchX = bLen, searchY = aLen;
		int curr = dp[aLen][bLen];
		while(LCS.length() < dp[aLen][bLen] ) {
			boolean next = false;
			for (int i = searchY; i >= 1; i--) {
				for (int j = searchX; j >= 1; j--) {
					if(a.charAt(i-1) == b.charAt(j-1) && dp[i][j] == curr) {
						LCS = (a.charAt(i-1) + LCS);
						curr -= 1;
						next = true;
						searchX = j - 1;
						searchY = i - 1;
						break;
					}
				}
				if(next)
					break;
			}
		}
		
		System.out.println(dp[aLen][bLen]);
		System.out.println(LCS);
	}
	
	public static void Union(int a, int b) {
		int x = Find(a);		// find parents
		int y = Find(b); 
		if(x != y) {
			parents[y] = x;
		}
	}
	
	public static int Find(int c) {
		if(parents[c] == c) {
			return c;
		} else {
			parents[c] = Find(parents[c]);
			return parents[c];
		}
	}
}