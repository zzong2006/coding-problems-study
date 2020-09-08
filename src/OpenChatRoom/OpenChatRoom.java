package OpenChatRoom;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

public class OpenChatRoom {
    public static void main(String[] args) {
        Solution a = new Solution();
        String[] ans = a.solution(new String[] {"Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"});
        for (String k: ans) {
            System.out.println(k);
        }
    }
}

class Solution {
    public String[] solution(String[] record) {
        String[] answer;
        ArrayList<StringBuilder> ans  = new ArrayList<>();
        HashMap<String, String> nickname = new HashMap<>();

        // build stringBuilder
        for (String chat : record){
            String[] sp = chat.split(" ");

            if(sp[0].compareTo("Enter") == 0){
                ans.add(new StringBuilder(sp[1] + "님이 들어왔습니다."));
                if(!nickname.containsKey(sp[1])){
                    nickname.put(sp[1], sp[2]);
                } else {
                    if(nickname.get(sp[1]).compareTo(sp[2]) != 0){
                        nickname.replace(sp[1], sp[2]);
                    }
                }
            } else if(sp[0].compareTo("Leave") == 0){
                ans.add(new StringBuilder(sp[1] + "님이 나갔습니다."));
            } else {            // Change
                if(!nickname.containsKey(sp[1])){
                    nickname.put(sp[1], sp[2]);
                } else {
                    if(nickname.get(sp[1]).compareTo(sp[2]) != 0){
                        nickname.replace(sp[1], sp[2]);
                    }
                }
            }

        }

        // change stringBuilder
        for (StringBuilder a : ans) {
            int idx = a.indexOf("님");
            String s = a.substring(0, idx);
            a.replace(0, idx, nickname.get(s));
        }

        // move stringBuilder to string
        answer = new String[ans.size()];
        for (int i = 0; i < ans.size(); i++) {
            answer[i] = ans.get(i).toString();
        }

        return answer;
    }
}