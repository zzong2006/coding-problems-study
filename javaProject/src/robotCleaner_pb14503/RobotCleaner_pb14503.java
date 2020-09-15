package robotCleaner_pb14503;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class RobotCleaner_pb14503 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int N, M;
		int [][] map;
		String [] inp = br.readLine().split(" ");
		
		N = stoi(inp[0]);
		M = stoi(inp[1]);
		
		map = new int [N][M];
		boolean[][] isCleaned = new boolean [N][M];
		String [] inp2 = br.readLine().split(" ");
		Robot rb = new Robot(stoi(inp2[1]), stoi(inp2[0]), stoi(inp2[2]));
		for (int i = 0; i < N; i++) {
			inp2 = br.readLine().split(" ");
			for (int j = 0; j < M; j++) {
				map[i][j] = stoi(inp2[j]);
				if(map[i][j] == 1) {
					isCleaned[i][j] = true;
				}
			}
		}
		
		rb.operate(isCleaned, map, N, M);
		
		System.out.println(rb.cleaningTimes);
	}
	public static int stoi(String a) {
		return Integer.parseInt(a);
	}
}

class Robot {
	int x;
	int y;
	int direction;
	//0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을
	int cleaningTimes;
	
	
	public Robot() {
		super();
	}


	public Robot(int x, int y, int direction) {
		super();
		this.x = x;
		this.y = y;
		this.direction = direction;
		this.cleaningTimes = 0;
	}

//	왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
//	왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
//	네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
//	네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
	
	public void operate(boolean [][] isCleaned, int [][] map, int N, int M) throws Exception {
		boolean stop = false;
		boolean cleaningMode = false;
		boolean movingMode = false;
		int alreadyCleaned = 0;
		while(!stop) {
			// 1. 현재 위치를 청소한다.
			if(!cleaningMode && !isCleaned[this.y][this.x]) {
				isCleaned[this.y][this.x] = true;
				cleaningTimes += 1;
				cleaningMode = true;
				movingMode = false;
			}
			
			// 2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
			// 2-1. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
			//0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을
			while(alreadyCleaned < 4 && !movingMode) {
				if(this.detectLeft(isCleaned, map, N, M)) {
					this.rotate();
					this.move();
					movingMode = true;
					cleaningMode = false;
					alreadyCleaned = 0;
				} else {
					this.rotate();
					alreadyCleaned += 1;
				}
			}
			
			if(alreadyCleaned >= 4) {
				alreadyCleaned = 0;
				movingMode = false;
				if(!this.moveBack(N, M, map)) {
					stop = true;
				}
			}
			
			
		}
		
	}
	
	public void rotate() throws Exception {
		//0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을
		switch(this.direction) {
		case 0:
			this.direction = 3;
			break;
		case 1:
			this.direction = 0;
			break;
		case 2:
			this.direction = 1;
			break;
		case 3:
			this.direction = 2;
			break;
		default:
			throw new Exception("Unknown Direction");
		}
	}
	public void move() throws Exception {
		//0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을
		switch(this.direction) {
		case 0:
			this.y -= 1;
			break;
		case 1:
			this.x += 1;
			break;
		case 2:
			this.y += 1;
			break;
		case 3:
			this.x -= 1;
			break;
		default:
			throw new Exception("Unknown Direction");
		}
	}
	public boolean moveBack(int N, int M, int[][] map) throws Exception {
		//0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을
		switch(this.direction) {
		case 0:
			if(this.y + 1 < N && map[this.y + 1][this.x] == 0) {
				this.y += 1;
				return true;
			} else 
				return false;
			
		case 1:
			if(this.x - 1 >= 0 && map[this.y][this.x - 1] == 0) {
				this.x -= 1;
				return true;
			} else 
				return false;
		case 2:
			if(this.y - 1 >= 0 && map[this.y - 1][this.x] == 0) {
				this.y -= 1;
				return true;
			} else 
				return false;
		case 3:
			if(this.x + 1 < M && map[this.y][this.x + 1] == 0) {
				this.x += 1;
				return true;
			} else 
				return false;
		default:
			throw new Exception("Unknown Direction");
		}
	}
	
	public boolean detectLeft(boolean [][] isCleaned, int [][] map, int N, int M) throws Exception {
		switch(this.direction) {
		//0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을
		case 0:
			if(this.x - 1 >= 0 && !isCleaned[this.y][this.x - 1] && map[this.y][this.x - 1] == 0) {
				return true;
			}else {
				return false;
			}
		case 1:
			if(this.y - 1 >= 0 && !isCleaned[this.y - 1][this.x] && map[this.y - 1][this.x] == 0) {
				return true;
			}else {
				return false;
			}
		case 2:
			if(this.x + 1 < M && !isCleaned[this.y][this.x + 1] && map[this.y][this.x + 1] == 0) {
				return true;
			}else {
				return false;
			}
		case 3:
			if(this.y + 1 < N && !isCleaned[this.y + 1][this.x] && map[this.y + 1][this.x] == 0) {
				return true;
			} else {
				return false;
			}
		default :
			throw new Exception("Unknown Direction");
		}
	}
}

