package coding_test.Kakao2020_5;

import java.util.ArrayList;
import java.util.Collections;

public class Kakao2020_5 {
    public static void main(String[] args) {
        Solution a = new Solution();
        String r;
//        r =a.solution("02:03:55", "00:14:15", new String[]{"01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"});
//        System.out.println("r = " + r);
//        r =a.solution("99:59:59", "25:00:00", new String[]{"69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"});
//        System.out.println("r = " + r);
        r =a.solution("50:00:00", "50:00:00", new String[]{"15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"});
        System.out.println("r = " + r);
    }
}
class Solution {
    public String solution(String play_time, String adv_time, String[] logs) {
        String answer = "";
        String [] ptVals = play_time.split(":");
        String [] advVals = adv_time.split(":");
        Time pt = new Time(Integer.parseInt(ptVals[0]),Integer.parseInt(ptVals[1]),Integer.parseInt(ptVals[2]));
        Time adt = new Time(Integer.parseInt(advVals[0]),Integer.parseInt(advVals[1]),Integer.parseInt(advVals[2]));
        TimeInterval [] tis = new TimeInterval[logs.length];

        for (int i = 0; i < logs.length; i++) {
            String [] spLogs = logs[i].split("-");
            String [] startLogs = spLogs[0].split(":");
            String [] endLogs = spLogs[1].split(":");

            tis[i] = new TimeInterval(Integer.parseInt(startLogs[0]),Integer.parseInt(startLogs[1]),Integer.parseInt(startLogs[2]),
                    Integer.parseInt(endLogs[0]),Integer.parseInt(endLogs[1]),Integer.parseInt(endLogs[2]));
        }

        // 앞에서 부터 찾음
        ArrayList<ADgap> res = new ArrayList<>();

        for (int i = 0; i < tis.length; i++) {
            // 구간 잡고
            Time endAd = tis[i].start.add(adt);
            if(endAd.isAhead(pt) <= 0){
                res.add(new ADgap(tis[i].start, 0));
                TimeInterval ad = new TimeInterval(tis[i].start.hour, tis[i].start.min, tis[i].start.sec,
                endAd.hour, endAd.min, endAd.sec);

                for (int j = 0; j < tis.length; j++) {
                    res.get(i).val += ad.getOverlap(tis[j]);
                }
            } else {
                res.add(new ADgap(tis[i].start, -1));
            }
        }

        // 뒤에서도 찾음
        for (int i = 0; i < tis.length; i++) {
            Time startAd = tis[i].end.sub(adt);
            if(startAd.hour >= 0 && startAd.min >= 0 && startAd.sec >= 0 &&
                    startAd.isAhead(new Time(0,0,0)) <= 0){
                res.add(new ADgap(startAd, 0));
                TimeInterval ad = new TimeInterval(startAd.hour, startAd.min, startAd.sec,
                        tis[i].start.hour, tis[i].start.min, tis[i].start.sec);

                for (int j = 0; j < tis.length; j++) {
                    res.get(res.size() - 1).val += ad.getOverlap(tis[j]);
                }
            } else {
                res.add(new ADgap(startAd, -1));
            }
        }
        
        // 가장 큰 구간 정렬
        Collections.sort(res, ((o1, o2) -> {
            if(o1.val > o2.val)
                return -1;
            else if (o1.val < o2.val){
                return 1;
            } else {
                if(o1.start.isAhead(o2.start) > 0){
                    return 1;
                } else if(o1.start.isAhead(o2.start) < 0){
                    return -1;
                } else {
                    return 0;
                }
            }
        }));

        // 출력
        Time ans;
        if(res.get(0).val != -1){
            ans = res.get(0).start;
        } else {
            ans = new Time(0,0,0);
        }
        answer =  "" + (ans.hour <= 9 ? "0" +ans.hour : ans.hour) + ":"
                + (ans.min <= 9 ? "0" +ans.min : ans.min)
                + ":" + (ans.sec <= 9 ? "0" +ans.sec : ans.sec) ;
        
        return answer;
    }
}

class ADgap{
    Time start;
    long val;

    public ADgap(Time start, long val) {
        this.start = start;
        this.val = val;
    }
}
class TimeInterval{
    Time start;
    Time end;

    public TimeInterval(int startH, int startM, int startS, int endH, int endM, int endS) {
        this.start = new Time(startH, startM, startS);
        this.end = new Time(endH, endM, endS);

    }

    public long getOverlap(TimeInterval a){
        long ans = 0;
        Time st, ed;
        if(this.start.isAhead(a.end) >= 0) { // 광고보다 왼쪽에 위치
            return 0;
        }
        if(a.start.isAhead(this.end) >= 0) {        // 광고보다 오른쪽에 위치
            return 0;
        }
        if(this.start.isAhead(a.start) >= 0){
            st = this.start;
        } else {
            st = a.start;
        }
        if(this.end.isAhead(a.end) >= 0){
            ed = a.end;
        } else {
            ed = this.end;
        }
        ans += st.gap(ed);
        return ans;
    }
}
class Time {
    int hour;
    int min;
    int sec;

    public Time(int hour, int min, int sec) {
        this.hour = hour;
        this.min = min;
        this.sec = sec;
    }
    public int  isAhead(Time a){
        if(a.hour > this.hour){
            return -1;
        } else if(a.hour < this.hour){
            return 1;
        } else {
            if(a.min > this.min){
                return -1;
            } else if(a.min < this.min){
                return 1;
            } else {
                if(a.sec > this.sec){
                    return -1;
                } else if(a.sec < this.sec){
                    return 1;
                }
            }
        }
        return 0;
    }

    public Time add(Time a){
        Time result = new Time(0,0,0);
        result.hour = this.hour + a.hour;
        result.min = this.min + a.min;
        result.sec = this.sec + a.sec;
        if(result.sec >= 60){
            result.sec -= 60;
            result.min += 1;
        }
        if(result.min >= 60){
            result.min -= 60;
            result.hour += 1;
        }
        return result;
    }
    public Time sub(Time b){
        Time higher, lower;
        Time result = new Time(0,0,0);

        result.hour = this.hour - b.hour;
        result.min = this.min - b.min;
        result.sec = this.sec - b.sec;
        if(result.sec < 0){
            result.sec += 60;
            result.min -= 1;
        }
        if(result.min < 0){
            result.min += 60;
            result.hour -= 1;
        }
        return result;
    }
    public int gap(Time a){
        Time higher = new Time(a.hour, a.min, a.sec),
                lower = new Time(this.hour, this.min, this.sec);
        int gapTime = 0;

        if(isAhead(a) < 0){
            higher = new Time(a.hour, a.min, a.sec);
            lower = new Time(this.hour, this.min, this.sec);
        } else {
            lower = new Time(a.hour, a.min, a.sec);
            higher = new Time(this.hour, this.min, this.sec);
        }

        int subSec = higher.sec - lower.sec ;
        if(subSec < 0) {
            gapTime += (60 + subSec);
            if(higher.min > 0)
                higher.min -= 1;
        } else{
            gapTime += subSec;
        }
        int subMin = higher.min - lower.min ;
        if(subMin < 0) {
            gapTime += ((60 + subMin) * 60);
            if(higher.hour > 0)
                higher.hour -= 1;
        } else{
            gapTime += (subMin * 60);
        }
        int subHour = higher.hour - lower.hour;
        gapTime += (subHour * 3600);

        return gapTime;
    }


}