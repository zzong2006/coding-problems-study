// https://programmers.co.kr/learn/courses/30/lessons/64065?language=java
// 프로그래머즈 : 튜플
// Note 1 : solution 2 가 되게 괜찮은 방법인거 같음 (다른 사람의 풀이)
// Note 2 : trim(), HashSet, replaceAll 기억할 것

package tupleProblem;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class tupleProblem {
    public static void main(String[] args) {
        Solution a = new Solution();
        int [] s = a.solution2("{{4,2,3},{3},{2,3,4,1},{2,3}}") ;
        for (int q: s) {
            System.out.print(q + " ");
        }
    }

}

class Solution {
    public int[] solution(String s) {
        int[] answer = {};

        int num = 0;
        String [] elms = s.substring(2, s.length() - 1).split("\\}");
        Element [] count = new Element[100001];
        for (int i = 0; i < count.length; i++) {
            count[i] = new Element(0, i);
        }
        for (int i = 0; i < elms.length; i++) {
            String [] a = elms[i].split(",");
            for (int j = 0; j < a.length; j++) {
                if(!a[j].isEmpty()){
                    int val = Integer.valueOf(a[j].replaceAll("[^0-9.]", ""));
                    count[val].count += 1;

                }
            }
        }

        Arrays.sort(count);
        answer = new int[elms.length];
        for (int i = 0; i < elms.length; i++) {
            answer[i] = count[i].val;
        }

        return answer;
    }

    public int[] solution2(String s) {
        Set<String> set = new HashSet<>();
        String[] arr = s.replaceAll("[{]", " ").replaceAll("[}]", " ").trim().split(" , ");
        Arrays.sort(arr, (a, b)->{return a.length() - b.length();});
        int[] answer = new int[arr.length];
        int idx = 0;
        for(String s1 : arr) {
            for(String s2 : s1.split(",")) {
                if(set.add(s2))
                    answer[idx++] = Integer.parseInt(s2);
            }
        }
        return answer;
    }
}

class Element implements Comparable{
    public int count = 0;
    public int val = 0;

    public Element(int count, int val) {
        this.count = count;
        this.val = val;
    }

    @Override
    public int compareTo(Object o) {
        Element a = (Element) o;
        if(a.count > this.count){
            return 1;
        } else
            return -1;
    }
}