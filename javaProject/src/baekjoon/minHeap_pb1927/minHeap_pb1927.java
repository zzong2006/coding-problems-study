package baekjoon.minHeap_pb1927;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class minHeap_pb1927 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int t = stoi(br.readLine());
		int [] minHeap = new int[100001];
		minHeap[0] = Integer.MIN_VALUE;
		int curr = 0;
		
		for (int i = 0; i < t; i++) {
			int g = stoi(br.readLine());
			if(g == 0) {	// pop
				if(curr == 0)
					System.out.println(curr);
				else {
					System.out.println(pop(minHeap, curr));
					curr -= 1;
				}
			} else {	// insert
				curr = insert(minHeap, g, curr);	
			}
		}
	}
	
	private static int pop(int[] minHeap, int curr) {
		int result = minHeap[1];
		int last = curr--;
		minHeap[1] = minHeap[last];
		int startIdx = 1;
		// Arrange
		while(startIdx * 2 + 1 <= curr ) {
			if(minHeap[startIdx * 2] < minHeap[startIdx * 2 + 1]) {
				if(minHeap[startIdx] > minHeap[startIdx * 2]) {
					swap(startIdx, startIdx * 2, minHeap);
				}
				startIdx *= 2;
			} else {
				if(minHeap[startIdx] > minHeap[startIdx * 2 + 1]) {
					swap(startIdx, startIdx * 2 + 1, minHeap);
				}
				startIdx *= 2;
				startIdx += 1;
			}
		}
		if(startIdx * 2 <= curr && minHeap[startIdx] > minHeap[startIdx * 2])
			swap(startIdx, startIdx * 2, minHeap);
		
		return result;
	}

	public static int stoi(String a) {
		return Integer.parseInt(a);
	}

	public static int insert(int [] minHeap, int val,  int curr) {
		// start with root;
		minHeap[++curr] = val;
		int insertIdx = curr;
		int temp = curr;
		
		while(insertIdx >= 2) {
			temp = insertIdx /2;
			if(minHeap[temp] > minHeap[insertIdx])
				swap(temp, insertIdx, minHeap);
			insertIdx /= 2;
		}
		return curr;
	}
	
	public static void swap(int a, int b, int [] nums) {
		int temp = nums[a];
		nums[a] = nums[b];
		nums[b] = temp;
	}
}
