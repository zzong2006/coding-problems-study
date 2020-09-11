package ParenthesisChange;

import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Stack;

public class ParenthesisChange {
    public static void main(String[] args) {
        Solution a = new Solution();

        String res = a.solution(")(");
        System.out.println("res = " + res);
        res = a.solution("()))((()");
        System.out.println("res = " + res);
    }
}

class Solution {
    public String solution(String w) {      // 균형잡힌 괄호 문자열 w
        String answer = "";

        if(w == "")     //  입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
            return "";
        else if(check(w)){
            return w;
        } else {
            // 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
            // 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
            String [] uv = split(w);
            if(check(uv[0])){
                answer = uv[0] + solution(uv[1]);
            } else {
                String emp = "(";
                emp = emp + solution(uv[1]) + ")";
                // u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
                StringBuilder u = new StringBuilder(uv[0]);
                u.deleteCharAt(u.length()-1);
                u.deleteCharAt(0);
                answer = emp + reverse(u.toString());
            }
        }
        return answer;
    }

    public String [] split(String h){
        int left = 0;
        int right = 0;
        int idx = 0;
        String [] ans = {"", ""};

        while(idx < h.length()){
            if(h.charAt(idx) == '('){
                left += 1;
            }  else {
                right += 1;
            }
            ans[0] += h.charAt(idx);
            if(left == right){
                break;
            }
            idx += 1;
        }
        ans[1] = h.substring(idx + 1);
        return ans;
    }

    public String reverse(String b){
        String ans = "";
        for (int i = 0; i < b.length(); i++) {
            if(b.charAt(i) == '(')
                ans += ")";
            else {
                ans += "(";
            }
        }
        return ans;
    }

    public boolean check(String a){
        if(a == "")
            return true;

        Stack<Character> st = new Stack<>();
        for (int i = 0; i < a.length(); i++) {
             if(a.charAt(i) == '('){
                 st.push('(');
             } else {
                 if(st.isEmpty()){
                     return false;
                 } else {
                     st.pop();
                 }
             }
        }
        if(st.isEmpty())
            return true;
        else
            return false;
    }
}