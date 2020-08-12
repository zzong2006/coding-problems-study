package printerQueue_1966;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Scanner;

class Main{
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// Scanner sc = new Scanner(System.in);
		int t = Integer.parseInt(br.readLine());
		
		for (int i=0; i<t; i++) {
			String[] input = br.readLine().split(" ");
			int n = Integer.parseInt(input[0]);
			int track = Integer.parseInt(input[1]);
			int [] remains = new int[10];
			queue que = new queue();
			int count = 0;
			
			input = br.readLine().split(" ");
			
			for (int j=0; j<n; j++) {
				int val = Integer.parseInt(input[j]);
				remains[val] += 1;
				que.push(val);
			}
			
			int curr = 0;
			for (int k=9; k>=0; k--) {
				if(remains[k] > 0) {
					curr = k;
					break;
				}
			}

			if(n == 1) {
				System.out.println("1");
			} else {
				while(!que.isEmpty()) {
					int pop_val = que.pop();
					if(pop_val == curr) {
						count += 1;
						if(track == 0) {
							break;
						} else {
							remains[curr] -= 1;
							if(remains[curr] == 0) {
								for (int k=curr-1; k>=0; k--) {
									if(remains[k] > 0) {
										curr = k;
										break;
									}
								}
							}
							track -= 1;
						}
					} else {
						que.push(pop_val);
						if(track == 0) {
							track = que.size() - 1;
						} else {
							track -= 1;
						}
					}
				}
				System.out.println(count);
			}
			
			
		}
	}
}

class queue {
	ArrayList<Integer> content ;
	
	public queue() {
		content = new ArrayList<>();
	}
	
	public int pop() {
		int val = this.content.get(0);
		this.content.remove(0);
		return val;
	}
	public void push(int a) {
		this.content.add(a);
	}
	
	public boolean isEmpty() {
		return this.content.isEmpty();
	}
	
	public int size() {
		return this.content.size(); 
	}
}

