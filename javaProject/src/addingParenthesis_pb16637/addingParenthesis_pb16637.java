package addingParenthesis_pb16637;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;


public class addingParenthesis_pb16637 {
	static long maxVal = Integer.MIN_VALUE ;
	static char [] ops ;
	static int [] nums ;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N;

		N = Integer.parseInt(br.readLine()); 
		
		String opsString = br.readLine();
		ops = new char [N/2];
		nums = new int [N/2 + 1];
		for (int i = 1; i <= N; i++) {
			if(i % 2 != 0) {
				nums[(i-1)/2] = opsString.charAt(i-1) - '0';
			} else {
				ops[(i-1)/2] = opsString.charAt(i-1);
			}
		}
		if(N != 1) {
			for (int i = 0; i < N/2 ; i++) {
				ArrayDeque <Integer> order = new ArrayDeque<>();
				order.add(i);
				getMaximumNum(order, N, i);
			}
		} else {
			maxVal = nums[0];
		}
		
		System.out.println(maxVal);
	}
	
	
	
	private static void getMaximumNum(ArrayDeque<Integer> order, int N, int currIdx) {
		
		if(currIdx < N/2 - 1) {
			if(order.getLast() == currIdx) {
				getMaximumNum(order, N, currIdx + 1);
			} else {
				ArrayDeque <Integer> otherOrder = order.clone();
				otherOrder.add(currIdx + 1);
				getMaximumNum(otherOrder, N, currIdx + 1);
				getMaximumNum(order, N, currIdx + 1);
			} 
			
		} else {	// start calculate
//			for (Integer integer : order) {
//				System.out.print(integer + " ");
//			}
//			System.out.println();
			
			int oprIdx , numCurr = 0, opsCurr = 0, oriNumCurr = 0, oriOpsCurr = 0;
			int [] changedNum = new int [N/2 + 1];
			char [] changedOps = new char [N/2];
			int lastCalNum = N/2 - order.size();
			
			while(!order.isEmpty()) {
				oprIdx = order.poll();
				while(oriOpsCurr < oprIdx ) {
					changedNum[numCurr++] = nums[oriNumCurr++];
					changedOps[opsCurr++] = ops[oriOpsCurr++];
				}
				if(ops[oriOpsCurr] == '-')
					changedNum[numCurr] = nums[oriNumCurr] - nums[oriNumCurr + 1];
				else if(ops[oriOpsCurr] == '*')
					changedNum[numCurr] = nums[oriNumCurr] * nums[oriNumCurr + 1];
				else // +
					changedNum[numCurr] = nums[oriNumCurr] + nums[oriNumCurr + 1];
				numCurr += 1; oriNumCurr += 2; oriOpsCurr += 1;
				if(oriOpsCurr < N/2 - 1) {
					changedOps[opsCurr++] = ops[oriOpsCurr++];
				}
			}
			while(oriOpsCurr < ops.length) {
				changedOps[opsCurr++] = ops[oriOpsCurr++];
			}
			while(oriNumCurr < nums.length)
				changedNum[numCurr++] = nums[oriNumCurr++];
			
			
			// calculate rest of them
			long lastVal = changedNum[0];

			for (int j = 0, k = 1; j < opsCurr; j++, k++) {
				if(changedOps[j] == '-') {
					lastVal -= changedNum[k];
				} else if (changedOps[j] == '*') {
					lastVal *= changedNum[k];
				} else {
					lastVal += changedNum[k];
				}
			} 
			maxVal = Math.max(lastVal, maxVal);
//			System.out.println(lastVal);
		}
	}
	
	
}