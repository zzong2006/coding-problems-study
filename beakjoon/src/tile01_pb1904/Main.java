package tile01_pb1904;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int input = Integer.parseInt(br.readLine());
		int [] caseOfTiles = new int [input + 10];
		caseOfTiles[0] = 0 ; caseOfTiles[1] = 1; caseOfTiles[2] = 2; 
		for (int i = 3; i <= input; i++) {
			caseOfTiles[i] = (caseOfTiles[i-1] + caseOfTiles[i-2]) % 15746;
			
		}
		bw.write(String.valueOf(caseOfTiles[input]));
		bw.flush();
	}
}
