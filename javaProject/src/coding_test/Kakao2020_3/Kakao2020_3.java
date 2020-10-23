package coding_test.Kakao2020_3;

import java.util.HashMap;
import java.util.HashSet;

public class Kakao2020_3 {
    public static void main(String[] args) {
        Solution a = new Solution();
        int []  res =a.solution(new String[]{"java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"}
                    , new String[]{"java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"});
        for (int re : res) {
            System.out.print(re + " ");
        }
    }
}

class Solution {
    public int[] solution(String[] info, String[] query) {
        int[] answer = {};
        answer = new int[query.length];
        // cpp, java, python, -
        HashSet<Integer> language [] = new HashSet[4];
        // backend, frontend, -
        HashSet<Integer> job [] = new HashSet[3];
        //  junior, senior, -
        HashSet<Integer> exp [] = new HashSet[3];
        // chicken, pizza, -
        HashSet<Integer> food [] = new HashSet[3];
        HashMap<Integer, Integer> score = new HashMap<>();

        HashSet<Integer> dp[][][][] = new HashSet[4][3][3][3];
        Boolean check[][][][] = new Boolean[4][3][3][3];
        for (int i = 0; i < check.length; i++) {
            check[i] = new Boolean[3][3][3];
            for (int j = 0; j < check[i].length; j++) {
                check[i][j] = new Boolean[3][3];
                for (int k = 0; k < check[i][j].length; k++) {
                    check[i][j][k] = new Boolean[3];
                    for (int l = 0; l < check[i][j][k].length; l++) {
                        check[i][j][k][l] = new Boolean(false);
                    }
                }
            }
        }
        for (int i = 0; i < 4; i++) {
            if(i != 3){
                language[i] = new HashSet<>();
                job[i] = new HashSet<>();
                exp[i] = new HashSet<>();
                food[i] = new HashSet<>();
            } else {
                language[i] = new HashSet<>();
            }
        }

        //build
        for (int i = 0; i < info.length; i++) {
            String [] infoS = info[i].split(" ");
            for (int j = 0; j < infoS.length; j++) {
                if(j == 0){ // cpp, java, python, -
                    if(infoS[j].compareTo("cpp") == 0){
                        language[0].add(i);
                    } else if (infoS[j].compareTo("java") == 0){
                        language[1].add(i);
                    } else if (infoS[j].compareTo("python") == 0){
                        language[2].add(i);
                    }
                } else if (j == 1){ // backend, frontend, -
                    if(infoS[j].compareTo("backend") == 0){
                        job[0].add(i);
                    } else if (infoS[j].compareTo("frontend") == 0){
                        job[1].add(i);
                    }
                } else if (j == 2){     // junior, senior, -
                    if(infoS[j].compareTo("junior") == 0){
                        exp[0].add(i);
                    } else if (infoS[j].compareTo("senior") == 0){
                        exp[1].add(i);
                    }
                } else if (j == 3){     // chicken, pizza, -
                    if(infoS[j].compareTo("chicken") == 0){
                        food[0].add(i);
                    } else if (infoS[j].compareTo("pizza") == 0){
                        food[1].add(i);
                    }
                } else {
                    int val = Integer.valueOf(infoS[j]);
                    score.put(i, val);
                }
            }
        }

        //do query
        for (int i = 0; i < query.length; i++) {
            String [] queryS = query[i].split(" and ");
            String [] remains = queryS[3].split(" ");
            queryS[3] = remains[0];
            int lIdx = -1, jIdx = -1, eIdx = -1, fIdx = -1, scoreVal = Integer.valueOf(remains[1]);
            for (int j = 0; j < queryS.length; j++) {
                if(j == 0){ // cpp, java, python, -
                    if(queryS[j].compareTo("cpp") == 0){
                        lIdx = 0;
                    } else if (queryS[j].compareTo("java") == 0){
                        lIdx = 1;
                    } else if (queryS[j].compareTo("python") == 0){
                        lIdx = 2;
                    } else {
                        lIdx = 3;
                    }
                } else if (j == 1){ // backend, frontend, -
                    if(queryS[j].compareTo("backend") == 0){
                        jIdx = 0;
                    } else if (queryS[j].compareTo("frontend") == 0){
                        jIdx = 1;
                    } else {
                        jIdx = 2;
                    }
                } else if (j == 2){     // junior, senior, -
                    if(queryS[j].compareTo("junior") == 0){
                        eIdx = 0;
                    } else if (queryS[j].compareTo("senior") == 0){
                        eIdx = 1;
                    } else {
                        eIdx = 2;
                    }
                } else if (j == 3){     // chicken, pizza, -
                    if(queryS[j].compareTo("chicken") == 0){
                        fIdx = 0;
                    } else if (queryS[j].compareTo("pizza") == 0){
                        fIdx = 1;
                    } else {
                        fIdx = 2;
                    }
                }
            }
            HashSet<Integer>Result = new HashSet<>();
            for (int j = 0; j < info.length; j++) {
                Result.add(j);
            }

            if(check[lIdx][2][2][2]){
                Result = new HashSet<>(dp[lIdx][2][2][2]);
            } else {
                if(lIdx != 3)
                    Result.retainAll(language[lIdx]);
                dp[lIdx][2][2][2] = new HashSet<>(Result);
                check[lIdx][2][2][2] = true;
            }

            if(check[lIdx][jIdx][2][2]){
                Result = new HashSet<>(dp[lIdx][jIdx][2][2]);
            } else {
                if(jIdx != 2)
                    Result.retainAll(job[jIdx]);
                dp[lIdx][jIdx][2][2] = new HashSet<>(Result);
                check[lIdx][jIdx][2][2] = true;
            }

            if(check[lIdx][jIdx][eIdx][2]){
                Result = new HashSet<>(dp[lIdx][jIdx][eIdx][2]);
            } else {
                if(eIdx != 2)
                    Result.retainAll(exp[eIdx]);
                dp[lIdx][jIdx][eIdx][2] = new HashSet<>(Result);
                check[lIdx][jIdx][eIdx][2] = true;
            }

            if(check[lIdx][jIdx][eIdx][fIdx]){
                Result = new HashSet<>(dp[lIdx][jIdx][eIdx][fIdx]);
            } else {
                if(fIdx != 2)
                    Result.retainAll(food[fIdx]);
                dp[lIdx][jIdx][eIdx][fIdx] = new HashSet<>(Result);
                check[lIdx][jIdx][eIdx][fIdx] = true;
            }

            int count = 0;
            for (Integer man : Result) {
                if(score.get(man) >= scoreVal)
                    count += 1;
            }
            answer[i] = count;
        }
        return answer;
    }
}