package baekjoon.givingARank_pb2012;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class givingARank_pb2012 {
	static int [] parents ;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = stoi(br.readLine());
		int [] arr = new int [n];
		for (int i = 0; i < n; i++) {
			arr[i] = stoi(br.readLine());
			
		}
		quickSort(0, n-1, arr);
		//Arrays.sort(arr);
		long curr = 1, sum = 0;
		for (int i = 0; i < n; i++) {
			sum += Math.abs(arr[i] - curr);
			curr += 1;
		}
		
		System.out.println(sum);
	}
	
	public static int stoi(String a) {
		return Integer.parseInt(a);
	}
	
	public static void quickSort(int start, int end, int [] nums) {
		if(start <= end) {
			int idx = start;
			
			for (int i = start ; i < end; i++) {
				if(nums[end] >= nums[i]) {
					int temp = nums[i];
					nums[i] = nums[idx];
					nums[idx] = temp;
					idx += 1;
				}
			}
			
			int temp = nums[end];
			nums[end] = nums[idx];
			nums[idx] = temp;
			quickSort(start, idx-1, nums);
			quickSort(idx+1, end, nums);
		}	
	}
}