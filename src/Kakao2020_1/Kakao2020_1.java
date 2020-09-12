package Kakao2020_1;

public class Kakao2020_1 {
    public static void main(String[] args) {
        Solution a = new Solution();
        String res ;
        res = a.solution("...!@BaT#*..y.abcdefghijklm");
        System.out.println("res = " + res);
        res = a.solution("z-+.^.");
        System.out.println("res = " + res);
        res = a.solution("=.=");
        System.out.println("res = " + res);
        res = a.solution("123_.def");
        System.out.println("res = " + res);
        res = a.solution("abcdefghijklmn.p");
        System.out.println("res = " + res);


    }
}
class Solution {
    public String solution(String new_id) {
        String answer = "";
        String lowerString = new_id.toLowerCase();
        String twoStep = "";
        for (int i = 0; i < lowerString.length(); i++) {
            Character w = lowerString.charAt(i);
            if( ('a' <= w && w <= 'z' )||
                    ('0' <= w && w <= '9' )
                || w == '-' || w == '_' || w == '.'){
                twoStep += lowerString.charAt(i);
            }
        }
        String threeStep ="";
        Character prev = twoStep.charAt(0);
        threeStep += prev;
        for (int i = 1; i < twoStep.length(); i++) {
            Character w = twoStep.charAt(i);

            if(prev == '.' && w == '.'){
                prev = w;
                continue;
            } else {
                threeStep += w;
            }
            prev = w;
        }
        String fourStep = "";
        for (int i = 0; i < threeStep.length(); i++) {
            if(i==0 && threeStep.charAt(i) == '.'){
                continue;
            }
            if(i == threeStep.length() - 1 && threeStep.charAt(i) =='.'){
                continue;
            }
            fourStep += threeStep.charAt(i);
        }
        // Five
        if(fourStep == ""){
            fourStep += "a";
        }
        String sixStep = "";
        if(fourStep.length() >= 16){
            if(fourStep.charAt(14) == '.'){
                sixStep = fourStep.substring(0, 14);
            } else {
                sixStep = fourStep.substring(0, 15);
            }
        } else {
            sixStep = fourStep;
        }
        while(sixStep.length() <= 2){
            sixStep += sixStep.charAt(sixStep.length()-1);
        }
        answer = sixStep;
        return answer;
    }
}