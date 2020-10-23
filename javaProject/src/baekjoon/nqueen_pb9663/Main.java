package baekjoon.nqueen_pb9663;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		ArrayList<Pointer> coords = new ArrayList<>();
		int count = 0;
		int [] curr = new int [n];
		Pointer[] candCoords = new Pointer[n];
		int currIdx = 0;
		
		for (int i = 0; i < n; i++) {
			candCoords[i] = new Pointer();
		}
		if(n != 1) {
			while (curr[0] != n) {
				if(curr[currIdx] >= n && currIdx != 0) {
					curr[currIdx] = 0;
					currIdx -= 1;
					curr[currIdx] += 1;
				} else {
					candCoords[currIdx].setPointer(currIdx, curr[currIdx]);
					if(currIdx != 0) {
						boolean decision = false;
						for (int j = 0; j < currIdx; j++) {
							decision |= checkOverlap(candCoords[j], candCoords[currIdx]);
						}
						if(!decision) {		// no overlap
							if(currIdx == n-1) {
								count += 1;
								curr[currIdx] += 1;
							} else {
								currIdx += 1;
							}
						} else {			// overlap occur
							curr[currIdx] += 1;	
						}
					} else {		// no queen in the board
						currIdx += 1;
					}
				}
			}
		} else {
			count = 1;
		}
		
		System.out.println(count);
	}
	
	public static boolean checkOverlap(Pointer a, Pointer b)
	{
		if(a.x == b.x)
			return true;
		if(a.y == b.y)
			return true;
		if(Math.abs(a.x - b.x) == Math.abs(a.y - b.y))
			return true;
		return false;
	}
	
}

class Pointer {
	public int x;
	public int y;
	
	public Pointer(int a, int b) {
		x = a;
		y = b;
	}
	
	public Pointer() {
		x = 0;
		y = 0;
	}
	
	public void setPointer(int x, int y) {
		this.x = x;
		this.y = y;
	}
}


//public static void disable(boolean [][] map, int n, int x, int y) {
//	// vertical and horizontal
//	for (int i = 0; i < n; i++) {
//		map[y][i] = true;
//		map[i][x] = true;
//	}
//	// Right Diagonal
//	int movedX = x;
//	int movedY = y;
//	while(movedX < n && movedY < n && movedX >= 0 && movedY >= 0) {
//		map[movedY--][movedX--] = true;
//	}
//	movedX = x;
//	movedY = y;
//	while(movedX < n && movedY < n && movedX >= 0 && movedY >= 0) {
//		map[movedY++][movedX++] = true;
//	}
//	movedX = x;
//	movedY = y;
//	while(movedX < n && movedY < n && movedX >= 0 && movedY >= 0) {
//		map[movedY++][movedX--] = true;
//	}
//	movedX = x;
//	movedY = y;
//	while(movedX < n && movedY < n && movedX >= 0 && movedY >= 0) {
//		map[movedY--][movedX++] = true;
//	}
//}

