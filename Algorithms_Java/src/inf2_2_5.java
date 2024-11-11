import java.util.*;
public class inf2_2_5 {
    public String solution(String[] votes, int k){

        Map<String, ArrayList<String>> pick = new HashMap<>();
        Map<String, Integer> thanks = new HashMap<>();

        for(String v : votes){
            String from = v.split(" ")[0];
            String to = v.split(" ")[1];
            if(pick.containsKey(to)){
                pick.get(to).add(from);
            }else{
                ArrayList<String> tmp = new ArrayList<>();
                tmp.add(from);
                pick.put(to, tmp);
            }
        }

        for(Map.Entry<String, ArrayList<String>> e: pick.entrySet()){
            if(e.getValue().size() >= k){
                for(String s : e.getValue()){
                    thanks.put(s,thanks.getOrDefault(s,0)+1);
                }
            }

        }

        int max = 0;
        for(Map.Entry<String,Integer> e: thanks.entrySet() ){
            if(e.getValue() >= max){
                max = e.getValue();
            }
        }

        String aheadName = "";

        for(Map.Entry<String,Integer> e: thanks.entrySet() ){
            if(e.getValue() == max){
                String key = e.getKey();
                if(aheadName.isEmpty()){
                    aheadName = key;
                }else{
                    aheadName = aheadName.compareTo(key) > 0 ? key : aheadName;
                }

            }
        }


        return aheadName;
    }

    public static void main(String[] args){
        inf2_2_5 T = new inf2_2_5();
        System.out.println(T.solution(new String[]{"john tom", "daniel luis", "john luis", "luis tom", "daniel tom", "luis john"}, 2));
        System.out.println(T.solution(new String[]{"john tom", "park luis", "john luis", "luis tom", "park tom", "luis john", "luis park", "park john", "john park", "tom john", "tom park", "tom luis"}, 2));
        System.out.println(T.solution(new String[]{"cody tom", "john tom", "cody luis", "daniel luis", "john luis", "luis tom", "daniel tom", "luis john"}, 2));
        System.out.println(T.solution(new String[]{"bob tom", "bob park", "park bob", "luis park", "daniel luis", "luis bob", "park luis", "tom bob", "tom luis", "john park", "park john"}, 3));
    }
}
