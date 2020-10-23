package baekjoon.sortInside_pb1427;

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
		int[] nums = new int[t.length()];
		int[] counts = new int [11];
		
		for (int i = 0; i < t.length(); i++) {
			int s = t.charAt(i) -'0';
			counts[s] += 1;
		}
		for(int s = 9; s >= 0; s--) {
			int w = counts[s];
			for (int i = 0; i < w; i++) {
				bw.write(s +'0');
			}
		}
		
		bw.flush();
	}
	
	public static void quick_sort(int start_idx, int end_idx, int[] nums){
		if(start_idx < end_idx) {
			int original_start = start_idx;
			int pivot = end_idx;
			
			for (int i = original_start; i <= end_idx; i++) {
				if(nums[i] < nums[pivot]) {
					swap(i, start_idx, nums);
					start_idx += 1;
				}
			}
			swap(start_idx, end_idx, nums);
			quick_sort(original_start, start_idx-1, nums);
			quick_sort(start_idx + 1, end_idx, nums);
		}
		
	}
	
	public static void swap (int a, int b, int [] nums) {
		int temp = nums[a];
		nums[a] = nums[b]; 
		nums[b] = temp;
	}
}
