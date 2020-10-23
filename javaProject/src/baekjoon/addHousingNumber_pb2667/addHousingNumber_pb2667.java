package baekjoon.addHousingNumber_pb2667;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Arrays;


public class addHousingNumber_pb2667 {
	static int[] parents;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int N = Integer.parseInt(br.readLine());
		// boolean [][][][] graphs = new boolean [N + 1][N + 1][N + 1][N + 1];
		boolean[][] availiable = new boolean[N + 1][N + 1];
		boolean[][] map = new boolean[N + 1][N + 1];
		int op = 0, a, b;
		for (int i = 1; i <= N; i++) {
			String input = br.readLine();
			for (int j = 1; j <= N; j++) {
				if (input.charAt(j - 1) - '0' == 1) {
					map[i][j] = true;
					availiable[i][j] = true;
				}
			}
		}

		int componentNum = 0;
		int curr = 0;
		Pointer node;
		ArrayDeque<Integer> deq = new ArrayDeque<>();
		int [] count = new int [N * N];
		node = FindUnvisited(availiable);
		
		while (node.getX() != -1 && node.getY() != -1) {
			node = FindUnvisited(availiable);
			if(node.getX() != -1 && node.getY() != -1) {
				BFS(map,  availiable, node, count, componentNum);
				componentNum += 1;
			}
		}
		System.out.println(componentNum);
		Arrays.sort(count);
		for (Integer teger : count) {
			if (teger != 0)
				System.out.println(teger);
		}
	}

	public static void BFS(boolean[][] graphs, boolean[][] avail, Pointer node, int[] count, int curr) {
		int x = node.getX();
		int y = node.getY();
		
		if (avail[y][x]) {
			avail[y][x] = false;
			count[curr] += 1;
			if(x - 1 >= 1  && avail[y][x - 1] && graphs[y][x - 1] == true) {
				BFS(graphs, avail, new Pointer( x - 1, y), count, curr);
			}
			
			if(x + 1 < graphs.length && avail[y][x + 1] && graphs[y][x + 1] == true) {
				BFS(graphs, avail, new Pointer(x + 1, y), count, curr);
			}
			
			if(y - 1 >= 1  && avail[y - 1][x] && graphs[y - 1][x] == true) {
				BFS(graphs, avail, new Pointer( x, y - 1), count, curr);
			}
			
			if(y + 1 < graphs.length && avail[y + 1][x] && graphs[y + 1][x] == true) {
				BFS(graphs, avail, new Pointer(x, y + 1 ), count, curr);
			}
		}
	}

	public static Pointer FindUnvisited(boolean[][] availiable) {
		for (int i = 1; i < availiable.length; i++) {
			for (int j = 1; j < availiable.length; j++) {
				if(availiable[i][j])
					return new Pointer(j, i);
			}
		}
		return new Pointer(-1, -1);
	}

}

class Pointer {
	public Pointer(int x, int y) {
		super();
		this.x = x;
		this.y = y;
	}
	public Pointer() {
		this.x = 0;
		this.y = 0;
	}
	int x;
	int y;
	
	public void setPointer(Pointer A) {
		this.x = A.x;
		this.y = A.y;
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
	public void incX() {
		this.x += 1;
	}
	public void decX() {
		this.x -= 1;
	}
	public void incY() {
		this.y += 1;
	}
	public void decY() {
		this.y -= 1;
	}	
	public boolean equals(Pointer A) {
		if( this.x == A.x && this.y ==A.y )
			return true;
		else
			return false;
	}
}