import java.util.ArrayList;

public class nPersonk {
    public static void main(String[] args) {
        int [] a = solution(4, 20);
        for (int i = 0; i < a.length; i++) {
            System.out.print(a[i] + " ");
        }
        System.out.println();

    }

    public static int[] solution(int n, long k) {
        ArrayList<Integer> answer  = new ArrayList<>();
        boolean [] visited = new boolean[n];
        recursive(answer, visited, n, k, n);
        int [] trueAnswer =  new int[n];
        for (int i = 0; i < n; i++) {
            trueAnswer[i] = answer.get(i);
        }
        return trueAnswer;
    }
    public static void recursive(ArrayList<Integer> ans, boolean [] visited, int n, long k, int trueN){
        if(ans.size() < trueN){
            if(ans.size() + 1 == trueN){
                for(int i = 0; i < trueN; i++){
                    if(!visited[i]){
                        visited[i] = true;
                        ans.add(i + 1);
                        return ;
                    }
                }
            } else {
                long a = getFactorial(n);
                long step = (a / n);
                long pos = (k-1) / step;
                int count = 0, i = 0;
                while(count < pos){
                    if(!visited[i]){
                        count += 1;
                        i += 1;
                    } else {
                        i += 1;
                    }
                }
                while(visited[i]){
                    i += 1;
                }
                visited[i] = true;
                ans.add(i + 1);
                recursive(ans, visited, n - 1, k - (step * pos), trueN);
            }

        }
    }
    public static int getFactorial(int n){
        if (n == 1)
            return 1;
        else {
            return n * getFactorial(n - 1);
        }
    }
}
