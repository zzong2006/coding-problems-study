import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;

public class justThatSong {
    public static void main(String[] args) throws Exception {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(solution("ABCDEFG", new String[] {"12:00,12:14,HELLO,CDEFGAB",
                                                    "13:00,13:05,WORLD,ABCDEF"} )+ "\n");
        bw.write(solution("CC#BCC#BCC#BCC#B", new String[] {"03:00,03:30,FOO,CC#B",
                "04:00,04:08,BAR,CC#BCC#BCC#B"})+ "\n");
            bw.write(solution("A#", new String[] {
                    "13:00,13:02,HAPPY3,B#A#"})+ "\n");
        bw.flush();
    }

    public static String solution(String m, String[] musicinfos) {
        ArrayList<Music> answer = new ArrayList<>();
        Music [] ms = new Music[musicinfos.length];
        for (int i = 0; i < musicinfos.length; i++) {
            ms[i] = new Music(musicinfos[i], i);
        }
        // count m's length
        int givenLength = 0;
        for (int i = 0; i < m.length(); i++) {
            if(m.charAt(i) != '#')
                givenLength += 1;
        }
        for (int i = 0; i < musicinfos.length; i++) {
            if(givenLength <= ms[i].length){
                if(ms[i].matchedSong(m)){
                    answer.add(ms[i]);
                }
            }
        }

        if(answer.size() > 0){
            Collections.sort(answer);
            return answer.get(0).title;
        } else {
            return "(None)";
        }

    }
}

class Music implements Comparable<Music>{
    Time startTime;
    Time endTime;
    String title;
    int length;
    int originalIdx;
    StringBuilder song;
    StringBuilder playedSong;

    Music(String infos, int idx){
        String [] inputs = infos.split(",");
        String [] start = inputs[0].split(":");
        String [] end = inputs[1].split(":");
        this.startTime = new Time(start[0], start[1]);
        this.endTime = new Time(end[0], end[1]);
        this.title = inputs[2];
        this.song = new StringBuilder(inputs[3]);
        this.length = this.startTime.getGap(this.endTime);
        this.originalIdx = idx;
        buildPlayedSong();
    }

    private void buildPlayedSong(){
        int curr = 0;
        this.playedSong = new StringBuilder("");
        StringBuilder temp = new StringBuilder("");
        int i = 0;
        while(i < this.length){
            temp.append(this.song.charAt(curr++));
            if(curr < this.song.length() && this.song.charAt(curr) == '#'){
                temp.append(this.song.charAt(curr++));
            }
            if(curr >= this.song.length())
                curr = 0;
            this.playedSong.append(temp);
            i += 1;
            temp.setLength(0);
        }
    }

    public boolean matchedSong(String m){
        int currSongIdx = 0, startIdx = 0;
        int objectSongIdx = 0;
        StringBuilder temp1 = new StringBuilder("");
        StringBuilder temp2 = new StringBuilder("");

        while(startIdx <= this.playedSong.length()  - m.length()){
            currSongIdx = startIdx;
            objectSongIdx = 0;
            boolean check = true;
            while(currSongIdx < this.playedSong.length() && objectSongIdx < m.length()){
                temp1.append(this.playedSong.charAt(currSongIdx++));
                if(currSongIdx < this.playedSong.length() && this.playedSong.charAt(currSongIdx) == '#'){
                    temp1.append(this.playedSong.charAt(currSongIdx++));
                }
                temp2.append(m.charAt(objectSongIdx++));
                if(objectSongIdx < m.length() && m.charAt(objectSongIdx) == '#'){
                    temp2.append(m.charAt(objectSongIdx++));
                }
                if(temp1.compareTo(temp2) != 0){
                    check = false;
                    break;
                }

            }
            if(temp1.charAt(temp1.length() - 1) == '#')
                startIdx += 2;
            else
                startIdx += 1;
            temp1.setLength(0);
            temp2.setLength(0);
            if(check){
                return true;
            }

        }
        return false;
    }

    public int compareTo(Music o) {
        int result = o.length - this.length;
        if(result == 0){
            result = this.originalIdx - o.originalIdx;
        }
        return result;
    }
}

class Time {
    int hour;
    int min;

    public Time(String hour, String min) {
        this.hour = Integer.parseInt(hour);
        this.min = Integer.parseInt(min);
    }

    public int getGap (Time a){
        if(this.hour == a.hour){
            if(a.min > this.min)
                return a.min - this.min;
            else
                return this.min - a.min;
        } else if (this.hour > a.hour){
            int diffMin = (this.hour - a.hour) * 60;
            diffMin += (this.min - a.min);
            return diffMin;
        } else {
            int diffMin = (a.hour - this.hour) * 60;
            diffMin += (a.min - this.min);
            return diffMin;
        }
    }
}
