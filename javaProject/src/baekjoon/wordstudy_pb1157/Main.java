package baekjoon.wordstudy_pb1157;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String t = br.readLine();
		t = t.toUpperCase();
		int [] counts = new int[300];
		for (int i = 0; i < t.length(); i++) {
			counts[t.charAt(i) - 'A'] += 1;
		}
		int max_val = 0, max_index = 0;
		for (int i = 0; i < counts.length; i++) {
			if (max_val < counts[i]) {
				max_index = i;
				max_val = counts[i];
			}
		}
		boolean multi = false;
		for (int i = 0; i < counts.length; i++) {
			if (max_val == counts[i] && max_index != i) {
				multi = true;
				break;
			}
		}
		if (multi) System.out.println("?");
		else System.out.println(Character.toChars(max_index + 'A'));
		
		
	}
}
