package blackjack;
import java.util.Scanner;
import java.util.ArrayList;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		int m = sc.nextInt();
		ArrayList<Integer> numbers = new ArrayList<>();
		
		for(int i=0; i<t; i++) {
			numbers.add(sc.nextInt());
		}
		int maxnum = 0;
		int tiny ;
		for(int j=0; j<numbers.size()-2;j++){

			for(int w=j + 1; w<numbers.size()-1;w++) {

				for(int k= w + 1;k<numbers.size();k++) {
					tiny = numbers.get(j)+numbers.get(w)+ numbers.get(k);
					if (tiny <= m) {
						maxnum = Math.max(maxnum, tiny);
					}
					
					
				}
			}
		}
		System.out.println(maxnum);
	}
}
