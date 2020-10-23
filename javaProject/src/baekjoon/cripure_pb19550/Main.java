package baekjoon.cripure_pb19550;


import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N, L;
		String [] input = br.readLine().split(" ");
		N = Integer.parseInt(input[0]); 
		L = Integer.parseInt(input[1]); 
		int [] num = new int [L + 1];
		boolean [] isCut = new boolean [N];
		Pointer [] lines = new Pointer[N];
		for (int i = 0; i < N; i++) {
			String [] input2 = br.readLine().split(" ");
			lines[i] = new Pointer(Integer.parseInt(input2[0]), Integer.parseInt(input2[1]));
		}
		
		increaseNum(num, lines, L);
		int count = 0;
		int maxIdx = 0;
		int cuttingTimes = 0;
		while(count < N) {
			maxIdx = findMax(num);
			count += cutRope(maxIdx, num, lines, isCut, L);
			cuttingTimes += 1;
		}
		
		System.out.println(cuttingTimes);
		
	}	
	
	private static int cutRope(int maxIdx, int[] num, Pointer[] lines, boolean[] isCut, int L) {
		int count = 0;
		for (int i = 0; i < lines.length; i++) {
			if(!isCut[i]) {
				if(Math.abs(lines[i].x - lines[i].y) <= (L-1)/2) {
					if(lines[i].x < lines[i].y) {
						if(lines[i].x <= maxIdx && maxIdx <= lines[i].y) {
							isCut[i] = true;
							count += 1;
							for (int j = lines[i].x; j <= lines[i].y; j++) {
								num[j] -= 1;
							}
						}
					} else {
						if(lines[i].y <= maxIdx && maxIdx <= lines[i].x) {
							isCut[i] = true;
							count += 1;
							for (int j = lines[i].y; j <= lines[i].x; j++) {
								num[j] -= 1;
							}
						}
					}
				} else {
					if(lines[i].x < lines[i].y) {
						if(!(lines[i].y <= maxIdx && maxIdx <= lines[i].x)) {
							isCut[i] = true;
							count += 1;
							for (int j = lines[i].y; j <= L-1; j++) {
								num[j] -= 1;
							}
							
							for (int j = 0; j <= lines[i].x; j++) {
								num[j] -= 1;
							}
						}
					} else {
						if(!(lines[i].x <= maxIdx && maxIdx <= lines[i].y)) {
							isCut[i] = true;
							count += 1;
							for (int j = lines[i].x; j <= L-1; j++) {
								num[j] -= 1;
							}
							
							for (int j = 0; j <= lines[i].y; j++) {
								num[j] -= 1;
							}
						}
					}
				}
			}
		}
		return count;
	}

	public static void increaseNum(int [] num, Pointer [] lines, int L) {
		int a, b;
		
		for (int i = 0; i < lines.length; i++) {
			if(Math.abs(lines[i].x - lines[i].y) <= (L-1)/2) {
				if(lines[i].x < lines[i].y) {
					for (int j = lines[i].x; j <= lines[i].y; j++) {
						num[j] += 1;
					}
				} else {
					for (int j = lines[i].y; j <= lines[i].x; j++) {
						num[j] += 1;
					}
				}
			} else {
				if(lines[i].x < lines[i].y) {
					for (int j = lines[i].y; j <= L-1; j++) {
						num[j] += 1;
					}
					
					for (int j = 0; j <= lines[i].x; j++) {
						num[j] += 1;
					}
				} else {
					for (int j = lines[i].x; j <= L-1; j++) {
						num[j] += 1;
					}
					
					for (int j = 0; j <= lines[i].y; j++) {
						num[j] += 1;
					}
				}
			}
		}
	}
	
	public static int findMax(int [] num) {
		int maxIdx = 0;
		int maxVal = num[0];
		
		for (int i = 1; i < num.length; i++) {
			if(num[i] > maxVal) {
				maxVal = num[i];
				maxIdx = i;
			}
		}
		return maxIdx;
	}
	
}

class Pointer{
	public int x;
	public int y;
	
	
	
	public Pointer(int x, int y) {
		super();
		this.x = x;
		this.y = y;
	}
	public int getX() {
		return x;
	}
	public void setX(int x) {
		this.x = x;
	}
	public int getY() {
		return y;
	}
	public void setY(int y) {
		this.y = y;
	}
	
}
