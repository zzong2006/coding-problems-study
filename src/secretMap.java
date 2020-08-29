import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class secretMap {
    public static void main(String[] args) {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int [] arr1 = {9, 20, 28, 18, 11};
        int [] arr2 = {30, 1, 21, 17, 28};
        solution(5, arr1, arr2);
        arr1 = new int[]{46, 33, 33, 22, 31, 50};
        arr2 = new int[]{27, 56, 19, 14, 14, 10};
        solution(6, arr1, arr2);
    }
    public static String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        String arr1Num;
        String arr2Num;
        for (int i = 0; i < arr1.length; i++) {
            String un = "";
            arr1Num = convertNumber(arr1[i], n);
            arr2Num = convertNumber(arr2[i], n);

            for (int j = 0; j < n; j++) {
                if(arr1Num.charAt(j) == '1' || arr2Num.charAt(j) == '1')
                    un += "#";
                else
                    un += " ";
            }
            answer[i] = new String(un);
        }

        return answer;
    }

    public static String convertNumber(int a, int n){
        String  ans = "";
        while(a >= 2){
            ans = a % 2 + ans;
            a /= 2;
        }
        ans = a + ans;
        while(ans.length() < n){
            ans = "0" + ans;
        }
        return ans;
    }
}

class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = {};
        return answer;
    }
}