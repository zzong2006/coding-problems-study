package ShuttleBus;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

public class ShuttleBus {
    public static void main(String[] args) {
        Solution a = new Solution();
        a.solution(1, 1, 5, new String[] {"08:00", "08:01", "08:02", "08:03"});
    }
}
class Solution {
    public String solution(int n, int t, int m, String[] timetable) {
        String answer = "";
        ArrayList<Crew> crews = new ArrayList<Crew>();
        for (int i = 0; i < timetable.length; i++) {
            String[] s = timetable[i].split(":");
            crews.add(new Crew(Integer.valueOf(s[0]), Integer.valueOf(s[1])));
        }
        Collections.sort(crews, new Comparator<Crew>() {
            @Override
            public int compare(Crew o1, Crew o2) {
                if(o1.t.hour != o2.t.hour)
                    return o1.t.hour - o2.t.hour;
                else
                    return o1.t.min - o2.t.min;
            }
        });

        return answer;
    }
}

class Crew {
    Time t;

    public Crew(int hour, int min) {
        t = new Time(hour,min);
    }

}

class Time {
    public int hour;
    public int min;

    public Time(int hour, int min) {
        this.hour = hour;
        this.min = min;
    }
}