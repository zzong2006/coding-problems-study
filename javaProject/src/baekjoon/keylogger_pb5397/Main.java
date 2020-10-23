package baekjoon.keylogger_pb5397;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

class Main{
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int t = Integer.parseInt(br.readLine());
		
		ArrayList<Integer> numbers = new ArrayList<>();

		
		char get_char;
		
		for(int i=0; i<t; i++) {
			StringBuilder result = new StringBuilder();
			stack lib_stack = new stack();
			stack saved_stack = new stack();
			String input = br.readLine();
			
			for (int j = 0; j < input.length(); j++) {
				if(input.charAt(j) == '<') {
					get_char = lib_stack.pop();
					if (get_char != '?') {
						saved_stack.push(get_char);
					}
				} else if (input.charAt(j) == '>') {
					get_char = saved_stack.pop();
					if (get_char != '?') {
						lib_stack.push(get_char);
					}
				} else if (input.charAt(j) == '-') {
					lib_stack.pop();
				} else {
					lib_stack.push(input.charAt(j));
				}
			}
			int ans_size = lib_stack.size();
			int rem_size = saved_stack.size();
			for(int k=0; k<ans_size; k++) {
				result.append(lib_stack.content.get(k));
			}
			for(int k=rem_size-1; k>=0; k--) {
				result.append(saved_stack.content.get(k));
			}
			System.out.println(result);	
		}
	}
}

class stack{
	int curr = -1;
	ArrayList<Character> content;
	public stack(){
		content = new ArrayList<>();
	}
	
	public char pop() {
		char val = '?';
		if (curr >= 0) {
			val = this.content.get(curr).charValue();
			this.content.remove(curr);
			curr -= 1;
		} 
		return val;
	}
	
	public void push(char a) {
		this.content.add(a);
		curr += 1;
	}
	
	public int size() {
		return this.content.size();
	}
}
