package findNumber_pb1920;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		String [] input = br.readLine().split(" ");
		int m = Integer.parseInt(br.readLine());
		String [] input2 = br.readLine().split(" ");
		int [] nums = new int [n];
		int [] finds_nums = new int [m];
		
		for (int i = 0; i < n; i++) {
			nums[i] = Integer.parseInt(input[i]);
		}
		Arrays.sort(nums);
		
		for (int i=0; i<m; i++) {
			boolean finded = false;
			int find_obj = Integer.parseInt(input2[i]);
			int start_idx = 0 , end_idx = n-1;
			int middle_idx = n/2;
			
			
			while (Math.abs(end_idx-start_idx) != 1) {
				if (nums[(middle_idx)] > find_obj) {
					end_idx = middle_idx;
				} else if(nums[(middle_idx)] < find_obj){
					start_idx = middle_idx;
				} else {
					finded = true;
					break;
				}
				middle_idx = (start_idx + end_idx)/2;
			}
			if(nums[start_idx] == find_obj || nums[end_idx] == find_obj) {
				finded = true;
			}
			if (finded) {
				System.out.println("1");
			} else {
				System.out.println("0");
			}
			
		}
		
	}
}
