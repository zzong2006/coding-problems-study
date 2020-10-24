package coding_test.주문표_변환하기;

import java.util.Scanner;

class Main {
    private static void solution(int numOfOrder, String[] orderArr) {
        // TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
        for (int i = 0; i < numOfOrder; i++) {
            StringBuilder ans = new StringBuilder();
            ans = dfs(orderArr[i], 0 );
            System.out.println(ans);
        }
    }
    static StringBuilder dfs(String str, int curr){
        StringBuilder result = new StringBuilder();
        for (int i = curr; i < str.length(); i++) {
            if( str.charAt(i) == ')'){
                break;
            }
            if (result.length() >= 1){
                char last_character = result.charAt(result.length() - 1);
                if('1' <= last_character && last_character <= '9' && str.charAt(i) == '('){
                    int times = (int) last_character - '0';
                    StringBuilder res = dfs(str, i + 1);
                    StringBuilder temp = new StringBuilder();
                    for (int j = 0; j < times; j++) {
                        temp.append(res);
                    }
                    result.deleteCharAt(result.length() - 1);
                    result.append(temp);
                    i += (1 + res.length());
                } else
                if('1' <= last_character && last_character <= '9' && 'A' <= str.charAt(i) && str.charAt(i) <= 'Z' ){
                    int times = (int) last_character - '0';
                    result.deleteCharAt(result.length() - 1);
                    for (int j = 0; j < times; j++) {
                        result.append(str.charAt(i));
                    }
                } else if ('A' <= last_character && last_character <= 'Z' && str.charAt(i) == '('){
                    StringBuilder res = dfs(str, i + 1);
                    StringBuilder temp = new StringBuilder();
                    for (int j = 0; j < res.length(); j++) {
                        temp.append(last_character);
                        temp.append(res.charAt(j));
                    }
                    result.deleteCharAt(result.length() - 1);
                    result.append(temp);
                    i += (1 + res.length());
                } else{
                    result.append(str.charAt(i));
                }

            } else{
                result.append(str.charAt(i));
            }

        }
        return result;
    }
    private static class InputData {
        int numOfOrder;
        String[] orderArr;
    }

    private static InputData processStdin() {
        InputData inputData = new InputData();

        try (Scanner scanner = new Scanner(System.in)) {
            inputData.numOfOrder = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));

            inputData.orderArr = new String[inputData.numOfOrder];
            for (int i = 0; i < inputData.numOfOrder; i++) {
                inputData.orderArr[i] = scanner.nextLine().replaceAll("\\s+", "");
            }
        } catch (Exception e) {
            throw e;
        }

        return inputData;
    }

    public static void main(String[] args) throws Exception {
        InputData inputData = processStdin();

        solution(inputData.numOfOrder, inputData.orderArr);
    }
}