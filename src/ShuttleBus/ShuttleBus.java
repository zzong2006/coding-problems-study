package ShuttleBus;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

public class ShuttleBus {
    public static void main(String[] args) {
        Solution a = new Solution();
        String ans = a.solution(2, 10, 2, new String[] {"09:10", "09:09", "08:00"});
        System.out.println("ans = " + ans);
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
        int busHour = 9;
        int busMin = 0;
        Bus [] bus = new Bus[n];
        for (int i = 0; i < n; i++) {
            bus[i] = new Bus(busHour, busMin, m);
            busMin += t;
            if(busMin >= 60){
                busMin %= 60;
                busHour += 1;
            }
        }
        // 각 크루는 어떤 버스에 탑승하는지 확인
        int currBus = 0;
        int currCrew = 0;
        while(currCrew < crews.size() && currBus < n){
            Crew crew = crews.get(currCrew);
            if(bus[currBus].arrive.compareTo(crew.t) >= 0 && bus[currBus].seat > 0){
                if(bus[currBus].seat == 1){
                    bus[currBus].crewIdx = currCrew;
                }
                bus[currBus].seat -= 1;

                crew.busIdx = currBus;
                currCrew += 1;
            } else {
                if(bus[currBus].arrive.compareTo(crew.t) < 0) {
                    currBus += 1;
                } else if(bus[currBus].seat <= 0){
                    currBus += 1;
                }
            }
        }
        Time cont = new Time(-1, -1);
        // 각 버스에 남는 자리 체크
        for (int i = bus.length - 1; i >= 0; i--) { // 가장 마지막 버스부터 확인 (자리 있으면 그 시간대)
            if(bus[i].seat > 0){
                answer = makeTimeToString(bus[i].arrive.hour , bus[i].arrive.min);
                break;
            } else {     // 만약 자리 없으면 새치기 가능한지 확인
                // 마지막 사람보다는 반드시 빨라야함
                cont.hour = crews.get(bus[i].crewIdx).t.hour;
                cont.min = crews.get(bus[i].crewIdx).t.min;
                cont.reduceOneMin();
                answer = makeTimeToString(cont);
                break;
            }
        }



        return answer;
    }

    String makeTimeToString(int hour, int min){
        String result = "";
        if(hour < 10){
            result += "0";
        }
        result += hour;

        result += ":";

        if(min < 10){
            result += "0";
        }
        result += min;

        return result;
    }

    String makeTimeToString(Time t){
        int hour = t.hour;
        int min = t.min;
        String result = "";
        if(hour < 10){
            result += "0";
        }
        result += hour;

        result += ":";

        if(min < 10){
            result += "0";
        }
        result += min;

        return result;
    }
}

class Crew {
    public Time t;
    public int busIdx;

    public Crew(int hour, int min) {
        t = new Time(hour,min);
        busIdx = -1;
    }

}

class Bus{
    public Time arrive;
    public int seat;
    public int crewIdx;

    public Bus(int hour, int min, int seat) {
        this.arrive = new Time(hour, min);
        this.seat = seat;
        this.crewIdx = -1;
    }
}
class Time implements Comparable{
    public int hour;
    public int min;

    public Time(int hour, int min) {
        this.hour = hour;
        this.min = min;
    }

    @Override
    public int compareTo(Object o) {
        Time to = (Time) o;
        if(to.hour == this.hour){
            return this.min - to.min;
        } else {
            return this.hour - to.hour;
        }
    }

    public void reduceOneMin(){
        if(this.hour != 0 || this.min != 0){
            this.min -= 1;
            if(this.min < 0){
                this.min += 60;
                this.hour -= 1;
            }
        }
    }
}