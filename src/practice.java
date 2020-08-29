import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class practice {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        bw.write(Integer.toBinaryString(5 | 8) + "\n");
        bw.write(Integer.toBinaryString(5) + "\n");
        bw.write(Integer.toBinaryString(8) + "\n");
        bw.flush();
        int n = 10;
        String result = String.format("%" + n + "s",Integer.toBinaryString(5 | 8));
        bw.write(result + "\n");
        bw.write(result.replaceAll("1", "#") + "\n");
        bw.write(result.replaceAll(" ", "0"));

        bw.flush();
    }
}
