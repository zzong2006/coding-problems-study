// https://programmers.co.kr/learn/courses/30/lessons/60057
// Note : 굳이 String을 만들 필요 없이 개수만 계산하면 되는 것임 (시간 나면 다시 풀기를 권장)

package stringCompression;

public class stringCompression {
    public static void main(String[] args) {
        Solution a = new Solution();

        System.out.println(a.solution("x"));
    }
}

class Solution {
    public int solution(String s) {
        int sLength = s.length();
        int answer = Integer.MAX_VALUE;
        for (int i = 1; i <= sLength / 2; i++) {
            // do compression
            String compressedStr = compression(s, i);

            // compare length
            answer = Math.min(compressedStr.length(), answer);
        }
        if(sLength == 1)
            answer = 1;
        return answer;
    }

    public String compression(String s, int step){
        int curr = 0;
        int count = 1;
        StringBuilder output = new StringBuilder("");
        String temp = "";
        while(curr + 2 * step - 1 < s.length()){
            temp = s.substring(curr, curr + step);
            if(temp.compareTo(s.substring(curr + step, curr + 2 * step)) == 0){
                count += 1;
            } else {
                output.append((count > 1 ? String.valueOf(count) : "") + temp);
                count = 1;
            }
            curr = curr + step;
        }
        if (count > 1){
            output.append((count > 1 ? String.valueOf(count) : "") + temp);
            output.append(s.substring(curr + step));
        } else {
            output.append(s.substring(curr));
        }

        return output.toString();
    }
}