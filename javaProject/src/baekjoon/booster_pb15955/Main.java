package baekjoon.booster_pb15955;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	static CheckPoint [] cps ;
	static Player you;
	static int start;
	static int goal;
	static boolean reachGoal;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n, q;
		String [] inp = br.readLine().split(" ");
		
		n = Integer.parseInt(inp[0]);
		q = Integer.parseInt(inp[1]);

		// check points
		cps = new CheckPoint[n];
		for (int i = 0; i < n; i++) {
			String [] xy = br.readLine().split(" ");
			cps[i] = new CheckPoint(Integer.parseInt(xy[0]), Integer.parseInt(xy[1]));
		}

		// do query
		for (int i = 0; i < q; i++) {
			String [] qr = br.readLine().split(" ");
			reachGoal = false;
			start = Integer.parseInt(qr[0]);
			goal = Integer.parseInt(qr[1]);
			you = new Player(cps[start].pos.x, cps[start].pos.y, Integer.parseInt(qr[2]));

			for (int j = 0; j < cps.length; j++) {
				canReach(j);
			}

			if(reachGoal){
				System.out.println("YES");
			} else {
				System.out.println("NO");
			}

		}
	}
	// DFS 로 하다가 중간에 뻑나면 기존꺼를 돌림
	public static void canReach(int cpIDX){
		if(reachGoal){
			return ;
		} else {
			if (you.goCheckPoint(cps[cpIDX])) {    // 현재 플레이어가 이 체크포인트에 접근 가능하다면 접근 후 부스터 및 hp 충전
				if(!you.booster){
					cps[cpIDX].booster = false;
					you.booster = true;
				}

				// 현재 상태 저장
				// 가능하면 재귀
			} else {
				return;
			}
		}
	}
}
class CheckPoint{
	Point pos;
	boolean heal;
	boolean booster;

	public CheckPoint(int x, int y) {
		this.pos = new Point(x, y);
		this.heal = true;
		this.booster = false;
	}
}

class Point {
	int x;
	int y;

	public Point(int x, int y) {
		this.x = x;
		this.y = y;
	}
}
class Player {
	int hp;
	int maxHp;
	boolean booster;
	Point pos;

	public Player(int hp, int x, int y) {
		this.hp = hp;
		this.maxHp = hp;
		this.pos = new Point(x, y);
		this.booster = false;
	}

	public void rechargeHp(CheckPoint a) {
		this.hp = this.maxHp;
		a.heal = false;
	}
	public void rechargeBooster(CheckPoint a){
		this.booster = true;
		a.booster = false;
	}

	public boolean goCheckPoint(CheckPoint cp){
		if(hp <= 0){
			if(booster){ 		// 직선거리에 있는지 확인
				if(cp.pos.x == this.pos.x && cp.pos.y != this.pos.y){
					this.booster = false;
					this.pos.y = cp.pos.y;
					return true;
				} else if(cp.pos.x != this.pos.x && cp.pos.y == this.pos.y) {
					this.booster = false;
					this.pos.x = cp.pos.x;
					return true;
				} else {
					return false;
				}
			} else {
				return false;
			}
		} else {
			double dist = Math.sqrt(Math.pow(cp.pos.x - this.pos.x, 2) + Math.pow(cp.pos.y - this.pos.y, 2));
			if( dist <= hp){
				hp -= dist;
				this.pos.x = cp.pos.x;
				this.pos.y = cp.pos.y;
				return true;
			} else{
				if(booster){
					if(Math.abs(cp.pos.x - this.pos.x) <= this.hp){
						this.hp -= Math.abs(cp.pos.x - this.pos.x);
						this.booster = false;
						this.pos.x = cp.pos.x;
						this.pos.y = cp.pos.y;
						return true;
					} else if(Math.abs(cp.pos.y - this.pos.y) <= this.hp){
						this.hp -= Math.abs(cp.pos.y - this.pos.y);
						this.booster = false;
						this.pos.x = cp.pos.x;
						this.pos.y = cp.pos.y;
						return true;
					} else {
						return false;
					}
				} else {
					return false;
				}
			}
		}
	}
}