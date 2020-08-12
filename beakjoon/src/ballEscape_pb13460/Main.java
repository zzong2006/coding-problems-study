package ballEscape_pb13460;

import java.util.Scanner;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

class Main{
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String [] input = br.readLine().split(" ");
		int n = Integer.parseInt(input[0]);
		int m = Integer.parseInt(input[1]);
		char [][] map = new char[n][m];
		Pointer red, blue, goal;
		red = null; blue = null; goal = null;
		
		for (int i = 0; i < n; i++) {
			String singleInput = br.readLine();
			for (int j = 0; j < m; j++) {
				map[i][j] = singleInput.charAt(j);
				if(map[i][j] == 'R') {
					red = new Pointer(j, i);
					map[i][j] = '.';
				}
					
				if(map[i][j] == 'B') {
					blue = new Pointer(j, i);
					map[i][j] = '.';
				}
					
				if(map[i][j] == 'O')
					goal = new Pointer(j, i);
			}
			
		}
		
		int currIdx = 0;
		int result = 0;
		int [] count = {-1};
		Situation [] curr = new Situation [12];
		curr[0] = new Situation(red, blue);
		
		solve(new Situation(red, blue), map, -1, 0, count, n, m);
		
		System.out.println(count[0]);
	}
	
	public static void solve(Situation st, char[][] map, int prev, int curr, int [] count, int n, int m) {
		Situation other;
		int result;
		if(curr >= 10 || count[0] == 1) 
			return ;
		else {
			curr += 1;
			if(prev != 1) {
				other = new Situation(st.getRed(), st.getBlue());
				result = other.goLeft(map, n, m);
				if(result == 0)			// move
					solve(other, map, 3, curr, count, n, m);
				else if(result == 1) {	// goal 
					if(count[0] == -1) 
						count[0] = curr;
					else {
						count[0] = Math.min(count[0], curr);
					}
				}
			} 
			if(prev != 3) {
				other = new Situation(st.getRed(), st.getBlue());
				result = other.goRight(map, n, m);
				if(result == 0)			// move
					solve(other, map, 1, curr, count, n, m);
				else if(result == 1) {	// goal 
					if(count[0] == -1) 
						count[0] = curr;
					else {
						count[0] = Math.min(count[0], curr);
					}
				}
			} 
			if(prev != 2) {
				other = new Situation(st.getRed(), st.getBlue());
				result = other.goUp(map, n, m);
				if(result == 0)			// move
					solve(other, map, 4, curr, count, n, m);
				else if(result == 1) {	// goal 
					if(count[0] == -1) 
						count[0] = curr;
					else {
						count[0] = Math.min(count[0], curr);
					}
				}
			} 
			if(prev != 4) {
				other = new Situation(st.getRed(), st.getBlue());
				result = other.goDown(map, n, m);
				if(result == 0)			// move
					solve(other, map, 2, curr, count, n, m);
				else if(result == 1) {	// goal 
					if(count[0] == -1) count[0] = curr;
					else {
						count[0] = Math.min(count[0], curr);
					}
				}
			} 
		}
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
	
	public void Pointer(Pointer A) {
		this.x = A.x;
		this.y = A.y;
	}
	
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
	
	public boolean goRight(char [][] map, int n, int m, Pointer opposite) {
		boolean goal = false;
		
		int y = this.getY();
		for (int i = this.getX() + 1; i < m; i++) {
			if(map[y][i] == 'O') {
				this.incX();
				goal = true;
				break;
			} else if(map[y][i] == '#' || (opposite.getX() == i && opposite.getY() == y) )
				break;
			else if(map[y][i] == '.') {
				this.incX();
			}
		}
		
		return goal;
	}
	
	public boolean goLeft(char [][] map, int n, int m, Pointer opposite) {
		boolean goal = false;
		
		int y = this.getY();
		for (int i = this.getX() - 1; i >= 0 ; i--) {
			if(map[y][i] == 'O') {
				this.decX();
				goal = true;
				break;
			} else if(map[y][i] == '#' || (opposite.getX() == i && opposite.getY() == y))
				break;
			else if(map[y][i] == '.') {
				this.decX();
			}
		}
		
		return goal;
	}
	
	public boolean goDown(char [][] map, int n, int m, Pointer opposite) {
		boolean goal = false;
		
		int x = this.getX();
		for (int i = this.getY() + 1; i < n; i++) {
			if(map[i][x] == 'O') {
				this.incY();
				goal = true;
				break;
			} else if(map[i][x] == '#' || (opposite.getX() == x && opposite.getY() == i))
				break;
			else if(map[i][x] == '.') {
				this.incY();
			}
		}
		
		return goal;
	}
	
	public boolean goUp(char [][] map, int n, int m, Pointer opposite) {
		boolean goal = false;
		
		int x = this.getX();
		for (int i = this.getY() - 1; i >= 0; i--) {
			if(map[i][x] == 'O') {
				this.decY();
				goal = true;
				break;
			} else if(map[i][x] == '#' || (opposite.getX() == x && opposite.getY() == i))
				break;
			else if(map[i][x] == '.') {
				this.decY();
			}
		}
		
		return goal;
	}
}

class Situation {
	public Situation(Pointer red, Pointer blue) {
		super();

		this.red = new Pointer();
		this.red.setPointer(red);
		this.blue = new Pointer();
		this.blue.setPointer(blue);
	}
	Pointer red;
	Pointer blue;
	int direction; // 1 : right, 2 : up , 3 : down, 4: left
	int prevDirection;
	
	public int getPrevDirection() {
		return prevDirection;
	}
	public void setPrevDirection(int prevDirection) {
		this.prevDirection = prevDirection;
	}
	public int getDirection() {
		return direction;
	}
	public void setDirection(int direction) {
		this.direction = direction;
	}
	
	public void incDirection() {
		direction += 1;
	}
	public Pointer getRed() {
		return red;
	}
	public void setRed(Pointer red) {
		this.red.setX(red.getX());
		this.red.setY(red.getY());
		
	}
	public Pointer getBlue() {
		return blue;
	}
	public void setBlue(Pointer blue) {
		this.blue.setX(blue.getX());
		this.blue.setY(blue.getY());
	}
	
	public int goRight(char [][] map, int n, int m) {
		boolean redGoal = false;
		boolean blueGoal = false;
		boolean redChanged = false;
		boolean blueChanged = false;
		Pointer temp = new Pointer();
		
		if(this.getRed().getX() < this.getBlue().getX()) {
			// Blue first
			temp.setPointer(this.getBlue());
			blueGoal = this.getBlue().goRight(map, n, m, this.getRed());
			if(!temp.equals(this.getBlue()))
				blueChanged = true;
			
			temp.setPointer(this.getRed());
			redGoal = this.getRed().goRight(map, n, m, this.getBlue());
			if(!temp.equals(this.getRed()))
				redChanged = true;
		} else {
			// Red first
			temp.setPointer(this.getRed());
			redGoal = this.getRed().goRight(map, n, m, this.getBlue());
			if(!temp.equals(this.getRed()))
				redChanged = true;
			
			temp.setPointer(this.getBlue());
			blueGoal = this.getBlue().goRight(map, n, m, this.getRed());
			if(!temp.equals(this.getBlue()))
				blueChanged = true;
		}
		
		if( (redGoal & blueGoal) || !(blueChanged | redChanged))
			return 3;
		else if(redGoal)
			return 1;
		else if(blueGoal)
			return 2;
		else 
			return 0;
	}
	
	public int goUp(char [][] map, int n, int m) {
		boolean redGoal = false;
		boolean blueGoal = false;
		boolean redChanged = false;
		boolean blueChanged = false;
		Pointer temp = new Pointer();
		
		if(this.getRed().getY() > this.getBlue().getY()) {
			// Blue first
			temp.setPointer(this.getBlue());
			blueGoal = this.getBlue().goUp(map, n, m, this.getRed());
			if(!temp.equals(this.getBlue()))
				blueChanged = true;
			
			temp.setPointer(this.getRed());
			redGoal = this.getRed().goUp(map, n, m, this.getBlue());
			if(!temp.equals(this.getRed()))
				redChanged = true;
		} else {
			// Red first
			temp.setPointer(this.getRed());
			redGoal = this.getRed().goUp(map, n, m, this.getBlue());
			if(!temp.equals(this.getRed()))
				redChanged = true;
			
			temp.setPointer(this.getBlue());
			blueGoal = this.getBlue().goUp(map, n, m, this.getRed());
			if(!temp.equals(this.getBlue()))
				blueChanged = true;
		}
		
		if( (redGoal & blueGoal) || !(blueChanged | redChanged))
			return 3;
		else if(redGoal)
			return 1;
		else if(blueGoal)
			return 2;
		else 
			return 0;
	}
	
	public int goDown(char [][] map, int n, int m) {
		boolean redGoal = false;
		boolean blueGoal = false;
		boolean redChanged = false;
		boolean blueChanged = false;
		Pointer temp = new Pointer();
		
		if(this.getRed().getY() < this.getBlue().getY()) {
			// Blue first
			temp.setPointer(this.getBlue());
			blueGoal = this.getBlue().goDown(map, n, m, this.getRed());
			if(!temp.equals(this.getBlue()))
				blueChanged = true;
			
			temp.setPointer(this.getRed());
			redGoal = this.getRed().goDown(map, n, m, this.getBlue());
			if(!temp.equals(this.getRed()))
				redChanged = true;
		} else {
			// Red first
			temp.setPointer(this.getRed());
			redGoal = this.getRed().goDown(map, n, m, this.getBlue());
			if(!temp.equals(this.getRed()))
				redChanged = true;
			
			temp.setPointer(this.getBlue());
			blueGoal = this.getBlue().goDown(map, n, m, this.getRed());
			if(!temp.equals(this.getBlue()))
				blueChanged = true;
		}
		
		if( (redGoal & blueGoal) || !(blueChanged | redChanged))
			return 3;
		else if(redGoal)
			return 1;
		else if(blueGoal)
			return 2;
		else 
			return 0;
	}
	
	public int goLeft(char [][] map, int n, int m) {
		boolean redGoal = false;
		boolean blueGoal = false;
		boolean redChanged = false;
		boolean blueChanged = false;
		Pointer temp = new Pointer();
		
		if(this.getRed().getX() > this.getBlue().getX()) {
			// Blue first
			temp.setPointer(this.getBlue());
			blueGoal = this.getBlue().goLeft(map, n, m, this.getRed());
			if(!temp.equals(this.getBlue()))
				blueChanged = true;
			
			temp.setPointer(this.getRed());
			redGoal = this.getRed().goLeft(map, n, m, this.getBlue());
			if(!temp.equals(this.getRed()))
				redChanged = true;
		} else {
			// Red first
			temp.setPointer(this.getRed());
			redGoal = this.getRed().goLeft(map, n, m, this.getBlue());
			if(!temp.equals(this.getRed()))
				redChanged = true;
			
			temp.setPointer(this.getBlue());
			blueGoal = this.getBlue().goLeft(map, n, m, this.getRed());
			if(!temp.equals(this.getBlue()))
				blueChanged = true;
		}
		
		if( (redGoal & blueGoal) || !(blueChanged | redChanged))
			return 3;
		else if(redGoal)
			return 1;
		else if(blueGoal)
			return 2;
		else 
			return 0;
	}
}