import java.util.Scanner;
import java.util.ArrayList;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int m = sc.nextInt();
		ArrayList<Integer> numbers = new ArrayList<>();
		ArrayList<Character> chars = new ArrayList<>();
		for(int i=0; i<m; i++) {
			numbers.add(i);
			chars.add('+');
		}
		for (int j=0; j<-1; j++) {
			System.out.println("Test");
		}
		for(int i=0; i<m; i++) {
			System.out.print(String.valueOf(numbers.get(i)) + " ");
			
		}
	}
}
