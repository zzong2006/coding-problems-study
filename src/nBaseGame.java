import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class nBaseGame {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int [] inputs = {16, 16, 2, 2};


        String ans = solution(inputs[0], inputs[1],inputs[2], inputs[3]);
        bw.write(ans);
        bw.flush();
    }

    public static String solution(int n, int t, int m, int p) {
        String answer = "";
        int trials = t;
        int startNumber = 0;
        String number = convertIntToBase(startNumber, n);
        int length = number.length();
        int curr = 0;
        while(trials != 0){
            for (int i = 0; i < m; i++) {
                if(i == p - 1){
                    answer += number.charAt(curr);
                    trials -= 1;
                }
                curr += 1;
                if(curr == length){
                    startNumber += 1;
                    number = convertIntToBase(startNumber, n);
                    length = number.length();
                    curr = 0;
                }
            }
        }


        return answer;
    }
    public static String convertIntToBase(int num, int base){
        String ans = "";
        String temp = "";
        while(num >= base){
            if((num % base) < 10){
                temp = (num % base) + "";
            } else {
                switch((num % base)){
                    case 10 :
                        temp = "A";
                        break;
                    case 11:
                        temp = "B";
                        break;
                    case 12:
                        temp = "C";
                        break;
                    case 13:
                        temp = "D";
                        break;
                    case 14:
                        temp = "E";
                        break;
                    case 15:
                        temp = "F";
                        break;
                }
            }
            ans = "" + temp + ans;
            num /= base;
        }
        if((num % base) < 10){
            temp = (num % base) + "";
        } else {
            switch((num % base)){
                case 10 :
                    temp = "A";
                    break;
                case 11:
                    temp = "B";
                    break;
                case 12:
                    temp = "C";
                    break;
                case 13:
                    temp = "D";
                    break;
                case 14:
                    temp = "E";
                    break;
                case 15:
                    temp = "F";
                    break;
            }
        }
        ans = "" + temp + ans;
        return ans;
    }
}


