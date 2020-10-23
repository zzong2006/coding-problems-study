package baekjoon.treeHeightWide_pb2250;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int input = Integer.parseInt(br.readLine());
		boolean [][] map = new boolean [10001][10001];
		int [] idx = {0};
		
		Tree root = null;
		for (int i = 0; i < input; i++) {
			String [] inputs = br.readLine().split(" ");
			Tree iterTree;
			if ( i == 0 ) {
				root = new Tree(Integer.parseInt(inputs[0]), i);
				iterTree = root;
			} else {
				iterTree= searchTree(root, Integer.parseInt(inputs[0]));
			}
			if(iterTree != null) {
				if(Integer.parseInt(inputs[1]) != -1)
					iterTree.insertLeft(Integer.parseInt(inputs[1]));
				if(Integer.parseInt(inputs[2]) != -1)
					iterTree.insertRight(Integer.parseInt(inputs[2]));
			} else {		// in case of not finding the item in the original tree
				Tree new_root = new Tree(Integer.parseInt(inputs[0]), 0);
				if(Integer.parseInt(inputs[1]) != -1)
					new_root.insertLeft(Integer.parseInt(inputs[1]));
				if(Integer.parseInt(inputs[2]) != -1)
					new_root.insertRight(Integer.parseInt(inputs[2]));
				
				int left_child = Integer.parseInt(inputs[1]);
				iterTree= searchTree(root, left_child);
				if(iterTree != null) {		// merge
					new_root.setLeft(iterTree);
					System.out.println("Error");
				}
				
			}
			
		}
		middleSearch(root, map, idx);
		int max_lvl = 0;
		int max_width = 0;
		for (int i = 0; i < 50000; i++) {
			int left = -1, right = -1;
			for (int j = 0; j <= idx[0]; j++) {
				if(map[i][j]) {
					left = j;
					break;
				}
			}
			for (int j = idx[0]; j >= 0; j--) {
				if(map[i][j]) {
					right = j;
					break;
				}	
			}
			int width = Math.abs(right-left+1);
			if(width > max_width) {
				max_lvl = i + 1;
				max_width = width;
			}
			if(left == -1 && right == -1)
				break;
		}
		System.out.println(max_lvl + " " + max_width);

	}
	
	public static Tree searchTree(Tree root, int i) {
		Tree sample = root;
		Queue<Tree> que = new LinkedList<>();
		que.add(sample);
		
		while(!que.isEmpty()) {
			sample = que.poll();
			if (sample != null ) {
				if(sample.getItem() == i)
					return sample;
				else {
					if(sample.getLeft() != null) {
						que.add(sample.getLeft());
					}
					if(sample.getRight() != null) {
						que.add(sample.getRight());
					}
				}
			}
		}
		return null;
	}
	
	// ���� ��ȸ
	public static void frontSearch(Tree itree) {
		System.out.print(itree.getItem() + " " + itree.getLevel());
		if (itree.getLeft() != null)
			frontSearch(itree.getLeft());
		if (itree.getRight() != null)
			frontSearch(itree.getRight());
		
	}
	public static void middleSearch(Tree itree, boolean [][] map, int [] idx) {
		if (itree.getLeft() != null)
			middleSearch(itree.getLeft(), map, idx);
		System.out.println(itree.getItem() + " " + itree.getLevel() + " " + idx[0]);
		map[itree.getLevel()][idx[0]++] = true;
		if (itree.getRight() != null)
			middleSearch(itree.getRight(), map, idx);
	}
	public static void backSearch(Tree itree) {
		if (itree.getLeft() != null)
			backSearch(itree.getLeft());
		if (itree.getRight() != null)
			backSearch(itree.getRight());
		System.out.print(itree.getItem());
	}
}

class Tree{
	Tree left = null;
	Tree right = null;
	boolean hasChild = true;
	int level = 0;
	int content ;
	
	public Tree(int c, int lv) {
		this.content = c;
		this.level = lv;
	}
	
	public Tree getLeft() {
		return left;
	}
	
	public Tree getRight() {
		return right;
	}
	
	public void setLeft(Tree lf) {
		this.left = lf;
	}
	
	public void setRight(Tree rt) {
		this.right = rt;
	}
	public int getItem() {
		return this.content;
	}
	
	public int getLevel() {
		return this.level;
	}
	public void insertRight(int c) {
		this.right = new Tree(c, this.level + 1);
		this.hasChild = true;
	}
	
	public void insertLeft(int c) {
		this.left = new Tree(c, this.level + 1);
		this.hasChild = true;
	}
	
	public boolean doesitHasChild() {
		return this.hasChild;
	}	
}
