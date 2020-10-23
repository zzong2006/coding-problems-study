package baekjoon.connectedComponent_pb11724;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;


public class connectedComponent_pb11724 {
	static int [] parents ;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N, M;
		String [] input = br.readLine().split(" ");
		N = Integer.parseInt(input[0]); 
		M = Integer.parseInt(input[1]); 
		boolean [][] graphs = new boolean [N + 1][N + 1];
		
		int op = 0, a, b;
		for (int i = 0; i < M; i++) {
			String [] input2 = br.readLine().split(" ");
			a = Integer.parseInt(input2[0]); 
			b = Integer.parseInt(input2[1]); 
			graphs[a][b] = true;
			graphs[b][a] = true; // undirected
		}
		boolean [] visited = new boolean [N + 1];
		int componentNum = 0;
		int visitiedCount = 0;
		int node;
		ArrayDeque<Integer> deq = new ArrayDeque<>(); 
		while((node = FindUnvisited(visited)) != -1) {
			BFS(graphs, deq, visited, node);
			componentNum += 1 ;
		}
		System.out.println(componentNum);
	}
	
	public static void BFS(boolean [][] graphs, ArrayDeque<Integer> deq, boolean [] visited, int node) {
		if(!visited[node]) {
			visited[node] = true;
			for (int i = 1; i < graphs[node].length; i++) {
				if(graphs[node][i] && !visited[i]) {
					BFS(graphs, deq, visited, i);
				}
			}
		}
	}
	
	public static int FindUnvisited(boolean [] visited) {
		for (int i = 1; i < visited.length; i++) {
			if(!visited[i])
				return i;
		}
		return -1;
	}
	public static void Union(int a, int b) {
		int x = Find(a);		// find parents
		int y = Find(b); 
		if(x != y) {
			parents[y] = x;
		}
	}
	
	public static int Find(int c) {
		if(parents[c] == c) {
			return c;
		} else {
			parents[c] = Find(parents[c]);
			return parents[c];
		}
	}
}