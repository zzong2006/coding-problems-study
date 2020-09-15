import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class autoComplete {
    public static void main(String[] args) throws Exception{
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        bw.write(solution(new String[] {"abbbb", "aabbb", "aaabb", "aaaab", "aaaaa"}) + "\n");
        bw.write(solution(new String[] {"go","gone","guild"}) + "\n");
        bw.write(solution(new String[] {"word", "war", "warrior", "world"}) + "\n");
        bw.flush();
    }
    public static int solution(String[] words) {
        int answer = 0;
        char temp ;
        int [] dp = new int [words.length];
        Arrays.sort(words);
        for (int i = 0; i < words.length; i++) {

            for (int j = dp[i]; j < words[i].length(); j++) {
                temp = words[i].charAt(j);
                boolean changed = false;
                for (int k = i + 1; k < words.length; k++) {
                    if( j < words[k].length() && dp[i] <= dp[k] && words[k].charAt(j) == temp){
                        dp[k] = dp[i] + 1;
                        changed = true;
                    } else {
                        break;
                    }
                }
                dp[i] += 1;
                if(!changed)
                    break;
            }
        }

        for (int i = 0; i < dp.length; i++) {
            answer += dp[i];
        }
        return answer;
    }
}
