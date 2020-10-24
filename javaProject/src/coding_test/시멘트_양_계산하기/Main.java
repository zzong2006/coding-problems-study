package coding_test.시멘트_양_계산하기;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Queue;
import java.util.Scanner;

class Main {
    private static void solution(int day, int width, int[][] blocks) {
        // TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
        int[] curr_height = new int[width];
        int answer = 0;
        for (int i = 0; i < day; i++) {
            for (int j = 0; j < width; j++) {
                curr_height[j] += blocks[i][j];
            }
            int[] left = new int[width];
            int[] right = new int[width];
            left[0] = curr_height[0];
            for (int j = 1; j < width; j++) {
                left[j] = Math.max(left[j - 1], curr_height[j]);
            }

            right[width - 1] = curr_height[width - 1];
            for (int j = width - 2; j >= 0; j--) {
                right[j] = Math.max(right[j + 1], curr_height[j]);
            }

            for (int j = 0; j < width; j++) {
                int min_height = Math.min(left[j], right[j]);
                if (min_height> curr_height[j]){
                    answer += (min_height - curr_height[j]);
                    curr_height[j] = min_height;
                }
            }
        }
        System.out.println(answer);
    }

    private static class InputData {
        int day;
        int width;
        int[][] blocks;
    }

    private static InputData processStdin() {
        InputData inputData = new InputData();

        try (Scanner scanner = new Scanner(System.in)) {
            inputData.day = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));
            inputData.width = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));

            inputData.blocks = new int[inputData.day][inputData.width];
            for (int i = 0; i < inputData.day; i++) {
                String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
                for (int j = 0; j < inputData.width; j++) {
                    inputData.blocks[i][j] = Integer.parseInt(buf[j]);
                }
            }
        } catch (Exception e) {
            throw e;
        }

        return inputData;
    }

    public static void main(String[] args) throws Exception {
        InputData inputData = processStdin();

        solution(inputData.day, inputData.width, inputData.blocks);
    }
}