package booster_pb15955;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n, q;
		String [] inp = br.readLine().split(" ");
		
		n = Integer.parseInt(inp[0]);
		q = Integer.parseInt(inp[1]);
		
		for (int i = 0; i < n; i++) {
			br.readLine().split(" ");
		}
		
		for (int i = 0; i < q; i++) {
			br.readLine().split(" ");
			System.out.println("NO");
		}
		
	}
}
