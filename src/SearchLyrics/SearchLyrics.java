package SearchLyrics;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

public class SearchLyrics {
    public static void main(String[] args) {
        Solution a = new Solution();
        int[] ans = a.solution(new String[] {"tertr", "rr", "tqe", "fe","retr0000000000000000000000000000000000000"},
                new String[] {"fro??", "????o", "?????", "??","azzz??????", "wqqs??","fr???", "fro???", "pro?","??","??????????????"});
        for (int i = 0; i < ans.length; i++) {
            int an = ans[i];
            System.out.print(an + " ");
        }
    }
}

class Solution {
    public int[] solution(String[] words, String[] queries) {
        int[] answer = new int[queries.length];
        Queries [] qr = new Queries[queries.length];
        for (int i = 0; i < queries.length; i++) {
            qr[i] = new Queries(i, queries[i]);
        }
        int maxLen = 0;
        for (int i = 0; i < words.length; i++) {
            maxLen = Math.max(words[i].length(), maxLen);
        }
        ArrayList<String>[] a = new ArrayList[maxLen + 1];
        for (int i = 0; i < a.length; i++) {
            a[i] = new ArrayList<>();
        }
        for (int i = 0; i < words.length; i++) {
            a[words[i].length()].add(words[i]);
        }

        Arrays.sort(qr, Comparator.comparing(o -> o.val));

        String prev = "";
        for (int i = 0; i < queries.length; i++) {
            if(queries[i].compareTo(prev) == 0){
                qr[i].matched = qr[i-1].matched;
                continue;
            } else {
                if(a.length <=  queries[i].length() || a[queries[i].length()].size() == 0){
                    qr[i].matched = 0;
                } else {
                    for (int j = 0; j < a[queries[i].length()].size(); j++) {
                        if(isMatched(a[queries[i].length()].get(j), qr[i].val, qr[i].val.charAt(0) == '?' ? 0 : 1)){
                            qr[i].matched += 1;
                        }
                    }
                }
            }
            prev = queries[i];
        }

        Arrays.sort(qr, (o1, o2) -> o1.idx - o2.idx);
        for (int i = 0; i < answer.length; i++) {
            answer[i] = qr[i].matched;
        }
        return answer;
    }

    private boolean isMatched(String a, String b, int s){
        if(s == 0) {        // 전위 (??ㅁㅁ)
            for (int i = b.length() - 1; i >= 0; i--) {
                if(b.charAt(i) == '?'){
                    return true;
                } else {
                    if(b.charAt(i) != a.charAt(i))
                        return false;
                }
            }
        } else {            // 후위 (ㅁㅁ??)
            for (int i = 0; i <= b.length(); i++) {
                if(b.charAt(i) == '?'){
                    return true;
                } else {
                    if(b.charAt(i) != a.charAt(i))
                        return false;
                }
            }
        }
        return true;
    }
}


class Queries {
    int idx ;
    String val;
    public int matched;

    public Queries(int idx, String val) {
        this.idx = idx;
        this.val = val;
        this.matched = 0;
    }
}