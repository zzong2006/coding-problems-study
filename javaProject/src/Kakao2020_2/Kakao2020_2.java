package Kakao2020_2;

import java.util.*;

public class Kakao2020_2 {
    public static void main(String[] args) {
        Solution a = new Solution();
        String [] res;
        res = a.solution(new String[]{"ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"},
                new int[] {2,3,4});
        for (int i = 0; i < res.length; i++) {
            String re = res[i];
            System.out.print(re + " ");
        }
        System.out.println();
        res = a.solution(new String[] {"XYZ", "XWY", "WXA"}, new int[] {2,3,4});

    }
}
class Solution {
    public String[] solution(String[] orders, int[] course) {
        String[] answer = {};
        ArrayList<String> result = new ArrayList<>();

        for (int i = 0; i < orders.length; i++) {
            String [] arr = orders[i].split("");
            Arrays.sort(arr);
            orders[i] = String.join("",arr);

        }
        HashMap<String, Integer>[] hm = new HashMap[11];
        for (int i = 0; i < hm.length; i++) {
            hm[i] = new HashMap<>();
        }
        for (int i = 0; i < orders.length; i++) {
            ArrayList<String> g = getAllComb(orders[i]);
            for (String s : g) {
                if(hm[s.length()].containsKey(s)){
                    int val = hm[s.length()].get(s);
                    val += 1;
                    hm[s.length()].replace(s, val);
                } else {
                    hm[s.length()].put(s, 1);
                }
            }
        }
        for (int i = 0; i < course.length; i++) {
            int n = course[i];
            int maxVal = 0;
            for(int val : hm[n].values()){
                maxVal = Math.max(maxVal, val);
            }
            if(maxVal >= 2) {
                for(String w : hm[n].keySet()){
                    if(hm[n].get(w) == maxVal)
                        result.add(w);
                }
            }
        }
        Collections.sort(result);
        answer = new String[result.size()];
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }
        return answer;
    }

    public ArrayList<String> getAllComb(String a){
        ArrayList<String> result = new ArrayList<>();
        int strLen = a.length();
        for (int i = 1; i < (1 << strLen); i++) {
            String em = "";
            for (int j = 0; j < strLen ; j++) {
                if( (i & (1 << j)) > 0){
                    em += a.charAt(j);
                }
            }
            if(em.length() > 1)
                result.add(em);
        }
        return result;
    }
}
