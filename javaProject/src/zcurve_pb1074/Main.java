package zcurve_pb1074;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String [] input = br.readLine().split(" ");		
		
		int n = Integer.parseInt(input[0]);
		int y = Integer.parseInt(input[1]);
		int x = Integer.parseInt(input[2]);
		
		curveValue((int)Math.pow(2, n-1), 0, 0, 0, y, x);
		

	}
	
	public static void curveValue(int step, int x, int y, int val, int ans_x, int ans_y) {
		if(step== 1) {
			if ( ans_x == x && ans_y == y) {
				System.out.print(val);
				return;
			} else if (ans_x == x  && ans_y == y + step) {
				System.out.print(val + 1);
			} else if (ans_x == x  + step&& ans_y == y) {
				System.out.print(val + 2);
				return;
			} else if (ans_x == x + step  && ans_y == y + step) {
				System.out.print(val + 3);
				return;
			}
		} else { // in case of step is 2, 4, 8, 16, ...
			int halfStep = step/2;
			int dStep = (int)Math.pow(step, 2);
			
			curveValue(halfStep, x, y, val + dStep * 0, ans_x, ans_y);
			curveValue(halfStep, x, y + step, val + dStep * 1, ans_x, ans_y);
			curveValue(halfStep, x + step, y, val + dStep * 2, ans_x, ans_y);
			curveValue(halfStep, x + step, y + step, val + dStep * 3, ans_x, ans_y);
			
		}
	}
}




class XYCoords <L, R> {
	L left;
	R right;
	
	public XYCoords(L left, R right){
		this.left = left;
		this.right = right;
	}
	
	public L getLeft() { return left; }
	public R getRight() { return right; }
}