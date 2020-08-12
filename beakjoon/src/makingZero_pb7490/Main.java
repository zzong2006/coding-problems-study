package makingZero_pb7490;


import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.Iterator;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int tc = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < tc; i++) {
			ArrayList<String> sl = new ArrayList<>();
			int num = Integer.parseInt(br.readLine());
			search(1, num, 0, 1, "", sl);
			Collections.sort(sl);
			
			for (int j = 0; j < sl.size(); j++) {
				bw = printOp(sl.get(j), num);
				bw.flush();
				System.out.println();
				
			}
			System.out.println();
		}
	}
	
	public static void search(int curr, int n, int sum, int val, String op, ArrayList<String> sl) throws IOException {
		if(curr == n) {
			if(sum + val == 0)	
				sl.add(op);
		} else  {
			int next = curr + 1;
			// '+'
			search(next , n, sum + val, next, op.concat("2"), sl);
			// '-'
			search(next , n, sum + val, -next, op.concat("3"), sl);
			// ' '
			int newVal;
			if (val < 0) {
				newVal = val * 10 - next;
			} else {
				newVal = val * 10 + next;
			}
			search(next, n, sum, newVal, op.concat("1"), sl);
		}
	}
	
	public static BufferedWriter printOp(String op, int num) throws IOException {
		int k = 1;
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		for (int i = 0; i < op.length(); i++) {
			String opSingle ;
			if(op.charAt(i) == '2') {
				opSingle = "+";
			} else if (op.charAt(i) == '3') {
				opSingle = "-";
			} else {
				opSingle = " ";
			}
			bw.write(String.valueOf(k)+opSingle);
			k += 1;
		}
		bw.write(String.valueOf(k));
		return bw;
	}
	
}

