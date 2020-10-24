package programmers.NewsClustering;

import java.util.HashMap;

public class NewsClustering {
    public static void main(String[] args) {
        Solution a = new Solution();
        int ans = a.solution("FRANCE", "french");
        System.out.println("ans = " + ans);
        ans = a.solution("handshake", "shake hands");
        System.out.println("ans = " + ans);
        ans = a.solution("aa1+aa2", "AAAA12");
        System.out.println("ans = " + ans);
        ans = a.solution("E=M*C^2", "e=m*c^2");
        System.out.println("ans = " + ans);

    }
}
class Solution {
    public int solution(String str1, String str2) {
        int answer = 0;
        HashMap<String, Integer> strMap1 = new HashMap<>();
        HashMap<String, Integer> strMap2 = new HashMap<>();
        String lowerStr1 = str1.toLowerCase();
        String lowerStr2 = str2.toLowerCase();

        insertString(lowerStr1, strMap1);
        insertString(lowerStr2, strMap2);

        answer = doJaccard(strMap1, strMap2);

        return answer;
    }

    private int doJaccard(HashMap<String, Integer> strMap1, HashMap<String, Integer> strMap2) {
        double intersection = 0.0;
        double union = 0.0;
        // intersection
        for (String s : strMap1.keySet()) {
            if(strMap2.containsKey(s)){
                intersection += Math.min(strMap1.get(s), strMap2.get(s));
            }
        }
        // union
        for (String s : strMap1.keySet()) {
            if(strMap2.containsKey(s)){
                union += Math.max(strMap1.get(s), strMap2.get(s));
            } else {
                union += strMap1.get(s);
            }
        }
        for (String s : strMap2.keySet()) {
            if(!strMap1.containsKey(s)){
                union += strMap2.get(s);
            }
        }

        if(union == 0 && intersection == 0){
            return 65536;
        } else {
            return (int)((intersection/union) * 65536);
        }
    }

    public void insertString(String str, HashMap<String, Integer> map){
        for (int i = 0; i < str.length() - 1; i++) {
            String a = str.substring(i, i + 2).replaceAll("[^a-z]", "");
            if(a.length() == 2){
                if(map.containsKey(a)){
                    int val = map.get(a) + 1;
                    map.replace(a, val);
                } else {
                    map.put(a, 1);
                }
            }
        }
    }
}

