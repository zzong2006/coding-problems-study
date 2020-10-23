package baekjoon.expressionOfSet_pb1717;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class expressionOfSet_pb1717 {
	static int [] parents ;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N, M;
		String [] input = br.readLine().split(" ");
		N = Integer.parseInt(input[0]); 
		M = Integer.parseInt(input[1]); 

		int [] children = new int [N+1];
		parents = new int [N+1];
		for (int i = 0; i < children.length; i++) {
			parents[i] = i;
			children[i] = i;
		}
		
		int op, a, b;
		for (int i = 0; i < M; i++) {
			String [] input2 = br.readLine().split(" ");
			op = Integer.parseInt(input2[0]); 
			a = Integer.parseInt(input2[1]); 
			b = Integer.parseInt(input2[2]); 
			if(op == 0) { // Union
				Union(a, b);
			} else if(op == 1) {
				if(Find(a) == Find(b))
					System.out.println("YES");
				else 
					System.out.println("NO");
			} else {
				throw new Exception();
			}
			
		}
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