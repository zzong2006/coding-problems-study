package Cache;

import java.util.HashMap;

public class Cache {
    public static void main(String[] args) {
        Solution a = new Solution();
        int t= a.solution(0, new String [] {"Jeju", "Pangyo", "NewYork", "newyork"});
        System.out.println("t = " + t);
    }
}
class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        int time = 0;
        HashMap<String, Integer> cache = new HashMap<>();

        for (String city : cities) {
            String lowerCity = city.toLowerCase();
            if(!cache.containsKey(lowerCity)){
                if(cache.size() < cacheSize){
                    cache.put(lowerCity, time);
                    time += 5;
                } else {    // find most unused item
                    if(cacheSize > 0) {
                        String unused = lowerCity;
                        int cacheTime = Integer.MAX_VALUE;
                        for (String s : cache.keySet()) {
                            if(cacheTime > cache.get(s)){
                                unused = s;
                                cacheTime = cache.get(s);
                            }
                        }
                        // delete unused item
                        cache.remove(unused);
                        cache.put(lowerCity, time);
                    }

                    time += 5;
                }
            } else { // cache hit
                cache.replace(lowerCity, time);
                time += 1;
            }
        }
        answer = time;
        return answer;
    }
}