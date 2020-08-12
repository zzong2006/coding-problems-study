package virus_pb2606;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Arrays;


public class virus_pb2606 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		
		boolean[][] map = new boolean[N + 1][N + 1];
		boolean [] visited = new boolean [N + 1];
		int  a, b;
		
		for (int i = 1; i <= M; i++) {
			String [] input = br.readLine().split(" ");
			a = Integer.parseInt(input[0]);
			b = Integer.parseInt(input[1]);
			map[a][b] = true;
			map[b][a] = true;
		}

		int componentNum = 0;
		ArrayDeque<Integer> deq = new ArrayDeque<>();
		int node = 1, count = -1;
		deq.offer(1);
		
		while(!(deq.isEmpty())) {
			node = deq.poll();
			if(!visited[node]) {
				visited[node] = true;
				count += 1;
				for (int i = 1; i < map[node].length; i++) {
					if(map[node][i] && !visited[i])
						deq.offer(i);
				}
			}
		}
		System.out.println(count);
		
	}

	public static int FindUnvisited(boolean[] visited) {
		for (int i = 1; i < visited.length; i++) {
			if(!visited[i])
				return i;
		}
		return -1;
	}

}
