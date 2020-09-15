package treeTour_pb1991;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int input = Integer.parseInt(br.readLine());
		Tree root = null;
		for (int i = 0; i < input; i++) {
			String [] inputs = br.readLine().split(" ");
			Tree iterTree;
			if ( i == 0 ) {
				root = new Tree(inputs[0].charAt(0));
				iterTree = root;
			} else {
				iterTree= searchTree(root, inputs[0].charAt(0));
			}
			
			if(inputs[1].charAt(0) != '.')
				iterTree.insertLeft(inputs[1].charAt(0));
			if(inputs[2].charAt(0) != '.')
				iterTree.insertRight(inputs[2].charAt(0));
		}
		frontSearch(root);
		System.out.println();
		middleSearch(root);
		System.out.println();
		backSearch(root);
	}
	
	public static Tree searchTree(Tree root, char c) {
		Tree sample = root;
		Queue<Tree> que = new LinkedList<>();
		que.add(sample);
		
		while(!que.isEmpty()) {
			sample = que.poll();
			if (sample != null ) {
				if(sample.getItem() == c)
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
	
	// 전위 순회
	public static void frontSearch(Tree itree) {
		System.out.print(itree.getItem());
		if (itree.getLeft() != null)
			frontSearch(itree.getLeft());
		if (itree.getRight() != null)
			frontSearch(itree.getRight());
		
	}
	public static void middleSearch(Tree itree) {
		if (itree.getLeft() != null)
			middleSearch(itree.getLeft());
		System.out.print(itree.getItem());
		if (itree.getRight() != null)
			middleSearch(itree.getRight());
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
	char content ;
	
	public Tree(char c) {
		this.content = c;
	}
	
	public Tree getLeft() {
		return left;
	}
	
	public Tree getRight() {
		return right;
	}
	
	public char getItem() {
		return this.content;
	}
	
	public void insertRight(char c) {
		this.right = new Tree(c);
		this.hasChild = true;
	}
	
	public void insertLeft(char c) {
		this.left = new Tree(c);
		this.hasChild = true;
	}
	
	public boolean doesitHasChild() {
		return this.hasChild;
	}
	
	
}
