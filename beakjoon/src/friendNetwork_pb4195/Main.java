package friendNetwork_pb4195;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;


public class Main {
	public static void main(String[] args) throws IOException {
		// Union-Find Algorithm ...
		// 참고한 알고리즘 : https://gmlwjd9405.github.io/2018/08/31/algorithm-union-find.html
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int t = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < t; i++) {
			int n = Integer.parseInt(br.readLine());
			// Parent, Child
			HashMap<String, String> friends = new HashMap<String, String>();
			HashMap<String, Integer> networks = new HashMap<String, Integer>();
			
			for (int j = 0; j < n; j++) {
				String[] input = br.readLine().split(" ");
				
				if (!friends.containsKey(input[0])) {
					friends.put(input[0], input[0]);
					networks.put(input[0], 1);
				}
				if (!friends.containsKey(input[1])) {
					friends.put(input[1], input[1]);
					networks.put(input[1], 1);
				}	
				
				Union(input[0], input[1], friends, networks);
				
				System.out.println(friends);
				System.out.println(networks);
				
				bw.write(networks.get(Find(input[0], friends)) + "\n");
			}
			
		}
		bw.flush();
	}
	
	public static void Union(String a, String b, HashMap<String, String> fr, HashMap <String, Integer> nt) {
		String x = Find(a, fr);
		String y = Find(b, fr);
		
		if (x != y) {
			fr.put(y, x);
			nt.put(x, nt.get(x) + nt.get(y));
		}
	}
	
	public static String Find(String a, HashMap<String, String> fr) {
		String pr = fr.get(a);
		if(fr.get(a) == a)
			return a;
		else {
			String temp = Find(pr,fr);	
			// find 하면서 만난 모든 값의 부모 노드를 root로 만든다.
			// fr.put(a, temp);
			return temp;
		}
	}
}
