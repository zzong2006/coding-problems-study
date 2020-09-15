package pb1874;

import java.util.Scanner;
import java.util.Stack;
import java.util.ArrayList;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		int curr_num = 0;
		int get_num = 0;
		int pop_num = 0;
		boolean ans = true;
		StringBuilder action = new StringBuilder();
		
		ArrayList<Integer> numbers = new ArrayList<>();
		// ArrayList<Character> action = new ArrayList<>();
		// Stack<Integer> lib_stack = new Stack<>();
		stack lib_stack = new  stack();
		
		for(int i=0; i<t; i++) {
			numbers.add(sc.nextInt());
		}
		
		for(int i=0; i<numbers.size(); i++) {
			get_num = numbers.get(i).intValue();
			if (curr_num <= get_num) {
				int repeat = get_num - curr_num;
				for(int j=0; j < repeat; j++) {
					action.append("+\n");
					curr_num += 1;
					lib_stack.push(curr_num);
				}
				action.append("-\n");
				pop_num = lib_stack.pop();
				
			} else {
				action.append("-\n");
				pop_num = lib_stack.pop();
			}
			if (pop_num != get_num) {
				ans = false;
				break;
			}
		}
		if (ans == false) {
			System.out.println("NO");
		} else {
			System.out.println(action);
		}
		
	}

}

class stack{
	int curr = -1;
	ArrayList<Integer> content;
	public stack(){
		content = new ArrayList<>();
	}
	
	public int pop() {
		int val = -1;
		if (curr >= 0) {
			val = this.content.get(curr).intValue(); 
			this.content.remove(curr);
			curr -= 1;
		} 
		return val;
	}
	
	public void push(int a) {
		this.content.add(a);
		curr += 1;
	}
}

