import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.Comparator;

public class sortingFileName {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String [] answer;
        answer = solution(new String[] {"img12.png", "img10.png", "img02.png", "img1.png",
                "IMG01.GIF", "img2.JPG"});
        for (int i = 0; i < answer.length; i++) {
            bw.write(answer[i] + " ");
        }
        bw.write("\n");

        answer = solution(new String[] {"F1500", "F33Z222", "F0002", "A99.txt"});
        for (int i = 0; i < answer.length; i++) {
            bw.write(answer[i] + " ");
        }

        bw.write("\n");
        bw.flush();
    }
    public static String[] solution(String[] files) {
        String[] answer = new String [files.length];
        fileName [] names = new fileName[files.length];
        for (int i = 0; i < files.length; i++) {
            StringBuilder temp = new StringBuilder(files[i]);
            names[i] = new fileName(temp);
        }

        Arrays.sort(names);


        for (int i = 0; i < files.length; i++) {
            answer[i] = names[i].returnToString();
        }
        return answer;
    }
}

class fileName implements Comparable<fileName> {
    StringBuilder head;
    int number;
    StringBuilder numberAsString;
    StringBuilder tail;

    fileName(StringBuilder a){
        int curr = this.splitUntilNumber(a);
        head = new StringBuilder(a.substring(0, curr));
        int num = this.splitUntilTail(a, curr);
        numberAsString = new StringBuilder(a.substring(curr, num));
        number = Integer.parseInt(numberAsString.toString());
        tail = new StringBuilder(a.substring(num));
    }

    private int splitUntilTail(StringBuilder a, int curr) {
        int i;
        for (i = curr; i < a.length(); i++) {
            if(!(a.charAt(i) - '0' >= 0 && a.charAt(i) -'0' <= 9)){
                break;
            }
        }
        return i;
    }

    private int splitUntilNumber(StringBuilder a) {
        int i;
        for (i = 0; i < a.length(); i++) {
            if(a.charAt(i) - '0' >= 0 && a.charAt(i) -'0' <= 9){
                break;
            }
        }
        return i;
    }

    public int compareTo(fileName o) {
        int result = this.head.toString().toLowerCase().compareTo(o.head.toString().toLowerCase());
        if (result == 0){
            result = this.number - o.number;
            return result;
        } else {
            return result;
        }
    }

    public String returnToString(){
        return ((head.append(numberAsString)).append(tail)).toString();
    }

}