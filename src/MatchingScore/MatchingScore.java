package MatchingScore;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class MatchingScore {
    public static void main(String[] args) {
        Solution a = new Solution();
        int idx = a.solution("blind", new String[] {
                "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  " +
                        "<meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  " +
                        "\n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. " +
                        "\n\n</body>\n</html>",
                "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  " +
                        "<meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  " +
                        "\n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"});
        System.out.println("idx = " + idx);
        idx = a.solution("Muzi", new String[] {"<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"});
        System.out.println("idx = " + idx);
    }
}

class Solution {
    public int solution(String word, String[] pages) {
        int answer = 0;
        WebPage [] wp = new WebPage[pages.length];

        for (int i = 0; i < wp.length; i++) {
            wp[i] = new WebPage(pages[i], i);
            wp[i].getBasic(word);
            wp[i].getOutLink();
        }
        for (int i = 0; i < wp.length; i++) {
            wp[i].getLinkAndMatching(wp);
        }
        Arrays.sort(wp);
        answer = wp[0].number;
        return answer;
    }
}

class WebPage implements Comparable{
    int basic;
    int outLink;
    double link;
    double matching;
    int number;
    String url;
    String html;
    String head;
    String body;
    ArrayList<String> outLinkList = new ArrayList<>();

    public WebPage(String html, int number) {
        this.html = html;
        this.head = html.substring(html.indexOf("<head>"), html.indexOf("</head>"));
        this.body = html.substring(html.indexOf("<body>"), html.indexOf("</body>"));
        this.number = number;
        this.basic = 0;
        int outLink = 0;
        int link = 0;

        // get URL
        int startMeta = this.head.indexOf("<meta property=\"og:url\" con");
        int startURL = this.head.indexOf("https://", startMeta);
        int endURL = this.head.indexOf("/>", startURL);

        this.url = this.head.substring(startURL, endURL - 1);
    }

    public void getBasic(String word){
        String lwWord = word.toLowerCase();
        String cst = this.html.toLowerCase().replaceAll("[^a-z]"," ");
        String [] cstS = cst.split(" ");
        for (String s : cstS) {
            if(s.compareTo(lwWord) == 0){
                this.basic += 1;
            }
        }
    }

    public void getOutLink(){
        int startURL = this.body.indexOf("<a href=\"");
        while(startURL != -1){
            startURL = this.body.indexOf("https://", startURL);
            int endURL = this.body.indexOf(">", startURL);
            outLinkList.add(this.body.substring(startURL, endURL - 1));
            startURL = endURL;
            startURL = this.body.indexOf("<a href=\"", startURL);
        }
        this.outLink = outLinkList.size();
    }

    @Override
    public int compareTo(Object o) {
        WebPage wp = (WebPage) o;
        if(this.matching == wp.matching){
            return this.number - wp.number;
        } else {
            if(this.matching - wp.matching >= 0)
                return -1;
            else
                return 1;
        }
    }

    public void getLinkAndMatching(WebPage[] wps) {
        for (int i = 0; i < wps.length; i++) {
            if(i != this.number){
                for (String ht : wps[i].outLinkList) {
                    if(ht.compareTo(this.url) == 0){
                        this.link += (wps[i].basic / (double)wps[i].outLink);
                    }
                }
            }
        }
        this.matching = this.basic + this.link;
    }
}