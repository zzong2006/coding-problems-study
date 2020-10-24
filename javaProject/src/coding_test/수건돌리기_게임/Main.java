package coding_test.수건돌리기_게임;

import java.util.HashMap;
import java.util.Scanner;

class Main {
    private static void solution(int numOfAllPlayers, int numOfQuickPlayers, char[] namesOfQuickPlayers, int numOfGames, int[] numOfMovesPerGame) {
        // TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
        int seats = numOfAllPlayers - 1;
        int[] players = new int[seats];
        HashMap<Integer, Integer> caught = new HashMap<>();
        caught.put(0, 1);

        for (int i = 1; i < numOfAllPlayers; i++) {
            players[i - 1] = i;
            caught.put(i, 0);
        }
        int tagger = 0;
        int tagger_pos = 0;
        for (int i = 0; i < numOfGames; i++) {
            tagger_pos += numOfMovesPerGame[i];

            if (tagger_pos < 0) {
                tagger_pos = seats + -(-tagger_pos % seats);
                tagger_pos %= seats;
            } else {
                tagger_pos %= seats;
            }
            // swap
            int temp = tagger;
            tagger = players[tagger_pos];
            players[tagger_pos] = temp;

            int time = caught.get(tagger);
            caught.replace(tagger, time + 1);

            // 술래인 사람이 빠른지 안빠른지 확인
            int fast_person = -1;
            for (int j = 0; j < numOfQuickPlayers; j++) {
                if (namesOfQuickPlayers[j] - 'A' == tagger) {
                    fast_person = j;
                    break;
                }
            }
            // 빠른 술래면 다시 원상 복구 시키고 게임 끝냄
            if (fast_person != -1) {
                // 빠른 사람은 술래가 안됨
                time = caught.get(tagger);
                caught.replace(tagger, time - 1);

                temp = tagger;
                tagger = players[tagger_pos];
                players[tagger_pos] = temp;

                time = caught.get(tagger);
                caught.replace(tagger, time + 1);
                break;
            }
        }


        // 12 시에 있는 사람 부터 이름 / 걸린 횟수
        for (int i = 0; i < players.length; i++) {
            if (tagger != players[i]) {
                System.out.println((char) (players[i] + (int) 'A') + " " + caught.get(players[i]));
            }

        }
        // 마지막에 걸린 술래 이름 / 걸린 횟수
        System.out.println((char) (tagger + (int) 'A') + " " + caught.get(tagger));
    }

    private static class InputData {
        int numOfAllPlayers;
        int numOfQuickPlayers;
        char[] namesOfQuickPlayers;
        int numOfGames;
        int[] numOfMovesPerGame;
    }

    private static InputData processStdin() {
        InputData inputData = new InputData();

        try (Scanner scanner = new Scanner(System.in)) {
            inputData.numOfAllPlayers = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));

            inputData.numOfQuickPlayers = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));
            inputData.namesOfQuickPlayers = new char[inputData.numOfQuickPlayers];
            System.arraycopy(scanner.nextLine().trim().replaceAll("\\s+", "").toCharArray(), 0, inputData.namesOfQuickPlayers, 0, inputData.numOfQuickPlayers);

            inputData.numOfGames = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));
            inputData.numOfMovesPerGame = new int[inputData.numOfGames];
            String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
            for (int i = 0; i < inputData.numOfGames; i++) {
                inputData.numOfMovesPerGame[i] = Integer.parseInt(buf[i]);
            }
        } catch (Exception e) {
            throw e;
        }

        return inputData;
    }

    public static void main(String[] args) throws Exception {
        InputData inputData = processStdin();

        solution(inputData.numOfAllPlayers, inputData.numOfQuickPlayers, inputData.namesOfQuickPlayers, inputData.numOfGames, inputData.numOfMovesPerGame);
    }
}