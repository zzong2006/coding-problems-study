import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class compression {
    public static void main(String[] args) throws Exception {

        printOutput(solution("KAKAO"));
        printOutput(solution("TOBEORNOTTOBEORTOBEORNOT"));
        printOutput(solution("ABABABABABABABAB"));

    }
    //LZW(Lempel–Ziv–Welch) 압축
    public static int[] solution(String msg) {
        ArrayList<Integer> ans = new ArrayList<>();
        ArrayList<dictionary> dic = new ArrayList<dictionary>();
        char Word = 'A' - 1;
        for (int i = 1; i <= 26; i++) {
            Word += 1;
            dic.add(new dictionary(i, new StringBuilder(Word + "")));
        }
        int curr = 0, output = -1, prev = 0;

        while(curr < msg.length()){
            StringBuilder currStr = new StringBuilder("");
            do {
                if(curr >= msg.length()){
                    if(prev > 0){
                        ans.add(prev);
                    }
                    break;
                }
                currStr.append(msg.charAt(curr++));
                output = searchFromRange(prev, currStr, dic);
                if(output > 0){
                    prev = output;
                } else {
                    // insert Words to Dictionary
                    dic.add(new dictionary(dic.size() + 1, currStr));
                    ans.add(prev);
                    curr -= 1;
                    prev = 0;
                }
            } while(output > 0);

        }

        int [] answer = new int [ans.size()];
        for (int i = 0; i < ans.size(); i++) {
            answer[i] = ans.get(i);
        }
        return answer;
    }

    public static int searchFromRange(int start, StringBuilder currStr, ArrayList<dictionary> dic){
        int loc = -1;
        dictionary ins;
        for (int i = start; i < dic.size(); i++) {
            ins = dic.get(i);
            if(ins.word.compareTo(currStr) == 0){
                return (i + 1);
            }
        }
        return loc;
    }

    public static void printOutput(int [] a) throws Exception{
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i = 0; i < a.length; i++) {
            bw.write(a[i] + " ");
        }
        bw.write("\n");
        bw.flush();
    }

}

class dictionary{
    int idxNumber;
    StringBuilder word;

    public dictionary(int idxNumber, StringBuilder word) {
        this.idxNumber = idxNumber;
        this.word = word;
    }

}
