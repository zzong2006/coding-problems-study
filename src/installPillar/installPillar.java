// https://programmers.co.kr/learn/courses/30/lessons/60061?language=java
// 프로그래머즈 : 기둥과 보 설치

package installPillar;

import java.util.ArrayList;
import java.util.Collections;

public class installPillar {
    public static void main(String[] args) {
//        System.out.println("[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]".replaceAll("[\\[]","\\{")
//        .replaceAll("\\]","\\}"));
        System.out.println("[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]".replaceAll("[\\[]","\\{")
        .replaceAll("\\]","\\}"));

        Solution a = new Solution();
        int [][] s = a.solution(5, new int[][] {{1,0,0,1},{1,1,1,1},{2,1,0,1},{2,2,1,1},{5,0,0,1},{5,1,0,1},{4,2,1,1},{3,2,1,1}}) ;
        for (int [] q: s) {
            for(int w : q){
                System.out.print(w + " ");
            }
            System.out.println();
        }

        System.out.println();

        s = a.solution(5, new int[][] {{0,0,0,1},{2,0,0,1},{4,0,0,1},{0,1,1,1},{1,1,1,1},{2,1,1,1},{3,1,1,1},{2,0,0,0},{1,1,1,0},{2,2,0,1},{0,1,0,1}}) ;
        for (int [] q: s) {
            for(int w : q){
                System.out.print(w + " ");
            }
            System.out.println();
        }
    }
}

class Solution {
    public int[][] solution(int n, int[][] build_frame) {
        int[][] answer = {};
        ArrayList<frame> frames = new ArrayList<>();
        for (int i = 0; i < build_frame.length; i++) {
            int x = build_frame[i][0];
            int y = build_frame[i][1];
            int type = build_frame[i][2];
            int buildType = build_frame[i][3]; // 0 은 삭제, 1은 설치

            if(buildType == 0){         // 삭제면 검사해서 무효화
                int deletedIDX = -1;
                frame deletedFrame = null;
                for (int j = 0; j < frames.size(); j++) {
                    frame temp = frames.get(j);
                    if(temp.x == x && temp.y == y && temp.type == type){
                        temp.installed = false;
                        deletedFrame = temp;
                        deletedIDX = j;
                        break;
                    }
                }
                // 삭제하고 해당 프레임들에게 다른 이상 없는지 검사
                for (int j = 0; j < frames.size(); j++) {
                    if(j != deletedIDX){
                        frame temp = frames.get(j);

                        if(!isSafe(temp, frames, n)){
                            deletedFrame.installed = true;
                            break;
                        }
                    }
                }

            } else {                    // 설치면 조건이 맞는지 검색
                frame candidate = new frame(x, y, type);

                if(isSafe(candidate, frames, n)){
                    frames.add(candidate);
                }
            }
        }
        int frSize = 0;
        for(frame tp : frames){
            if(tp.installed)
                frSize += 1;
        }
        Collections.sort(frames);

        answer = new int[frSize][3];
        int curr = 0;
        for (int i = 0; i <frames.size(); i++) {
            frame temp = frames.get(i);
            if(temp.installed){
                answer[curr][0] = temp.x;
                answer[curr][1] = temp.y;
                answer[curr][2] = temp.type;
                curr += 1;
            }
        }
        return answer;
    }

    public boolean isSafe(frame input, ArrayList<frame> frames, int n){
        boolean condition = false;

        if(input.type == 1){      // 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
            boolean leftConnected = false;
            boolean rightConnected = false;
            for (frame temp : frames) {
                if(temp.installed &&
                        !(temp.x == input.x && temp.y == input.y && temp.type == input.type)){
                    if(temp.type == 0){         // 한쪽 끝 부분이 해당 기둥 위에 있어야 함
                        if((input.x == temp.x  && input.y == temp.y + 1)
                                || (input.x + 1 == temp.x && input.y == temp.y + 1)){
                            condition = true;
                            break;
                        }
                    }
                    if(temp.type == 1) {        // 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 함
                        if( temp.x + 1 == input.x && temp.y == input.y){
                            leftConnected = true;
                        }
                        if( temp.x == input.x + 1 && temp.y == input.y){
                            rightConnected = true;
                        }
                    }
                }
            }

            condition |= (leftConnected & rightConnected);
        } else {            // 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
            if(input.y == 0){     // 바닥 위
                condition = true;
            } else {
                for (frame temp : frames) {
                    if(temp.installed &&
                            !(temp.x == input.x && temp.y == input.y && temp.type == input.type)){
                        if (temp.type == 0 && temp.x == input.x  && temp.y + 1 == input.y  ) {         // 해당 기둥 위에 있어야함
                            condition = true;
                            break;
                        }
                        if (temp.type == 1) {      // 해당 보의 한쪽 끝 부분 위에 있어야 함
                            if ((temp.x == input.x && temp.y == input.y) || ( temp.x + 1 == input.x && temp.y == input.y)) {
                                condition = true;
                                break;
                            }
                        }
                    }
                }
            }
        }

        return condition;
    }
}

// 기둥
class frame implements Comparable{
    public int x;
    public int y;
    public int type;       // 0 은 기둥, 1 은 보
    public boolean installed;

    public frame(int x, int y, int type) {
        this.x = x;
        this.y = y;
        this.type = type;
        this.installed = true;
    }

    @Override
    public int compareTo(Object o) {
        frame temp = (frame) o;
        if(temp.x != this.x){
            return this.x - temp.x;
        } else if(temp.y != this.y){
            return this.y - temp.y;
        } else {
            return this.type - temp.type;
        }
    }
}

// 아래의 코드는 모든 frame을 직접 검사하는 것이 아니라 삭제된 frame 근처의 frame만 검사할 경우 사용하는 코드임
// 제출 후 시간을 측정해보니 충분히 빨라서 아래 코드는 그냥 사용 안하는 것으로 둠

//                        if(deletedFrame.type == 0){     // 삭제된 기둥의 경우
//                            // 1. 기둥 위로 좌,우 보 그리고 상단 기둥 검사
//                            if(temp.type == 0 && temp.x == deletedFrame.x){
//                                if(temp.y == deletedFrame.y + 1){           // 상단
//                                    condition &= isSafe(temp, frames, n);
//                                }
//                                if(temp.y == deletedFrame.y - 1){           // 하단
//                                    condition &= isSafe(temp, frames, n);
//                                }
//                            }
//                            // 2. 기둥 아래로 좌우 그리고 하단 기둥 검사
//                            if(temp.type == 1){
//                                if(temp.x == deletedFrame.x){           // 우 보
//                                    if(temp.y )                         // 상단
//                                } else if(temp.x + 1 == deletedFrame.x){    // 좌 보
//
//                                }
//                            }
//                        } else {                        // 삭제된 보의 경우
//                            // 1. 보 왼쪽으로 하단 상단 기둥 그리고 왼쪽에 붙은 보 검사
//
//                            // 2. 보 오른쪽으로 하단 상단 기둥 그리고 오른쪽에 붙은 보 검사
//
//                        }