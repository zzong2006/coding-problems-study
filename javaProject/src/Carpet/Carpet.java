package Carpet;

//iter    Iterate (for each..in)
//        itin    Iterate (for..in)
//        itli    Iterate over a List
//        itar    Iterate elements of array
//        ritar   Iterate elements of array in reverse order
//        sout  System.out.println
public class Carpet {
    public static void main(String[] args) {
        Solution a = new Solution();
        int [] s = a.solution(8,1);
        for (int i : s) {
            System.out.println("i = " + i);
        }
    }
}
class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int [2];
        String someText = "This code can be on a single line " +
                "or it can be on multiple lines " +
                "and you can type and hit Enter and get the + sign " +
                "inserted automatically";
        int width = 2;
        int height = 2;
        do{
            height += 1;
            if((brown + yellow) % height != 0){
                width = (brown + yellow) / height;
                continue;
            } else {
                width = (brown + yellow) / height;
                if(height * 2 + width * 2 - 4 == brown){
                    answer[0] = width ; answer[1] = height;
                    break;
                }
            }
        }while(width >= height);

        return answer;
    }
}