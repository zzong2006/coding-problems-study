package sorting_pb2750;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int t = Integer.parseInt(br.readLine());
		int[] nums = new int [t];
		
		for (int i = 0; i < t; i++) {
			int s = Integer.parseInt(br.readLine());
			nums[i] = s;
		}
		quick_sort(0, nums.length-1, nums.length,nums);
		
		for (int i = 0; i < nums.length; i++) {
			bw.write(nums[i] + "\n");
		}
		
		bw.flush();
	}
	
	public static void quick_sort(int start_idx, int end_idx, int pivot, int[] nums){
		if(start_idx < end_idx) {
			int original_start = start_idx;
			pivot = end_idx;
			// int j = start_idx;
			
			for (int i = original_start; i < end_idx; i++) {
				if(nums[i] < nums[pivot]) {
					swap(i, start_idx, nums);
					start_idx += 1;
				}
			}
			swap(start_idx, end_idx, nums);
			quick_sort(original_start, start_idx-1, start_idx, nums);
			quick_sort(start_idx + 1, end_idx, end_idx, nums);
		}
		
	}
	
	public static void swap (int a, int b, int [] nums) {
		int temp = nums[a];
		nums[a] = nums[b]; 
		nums[b] = temp;
	}
}
