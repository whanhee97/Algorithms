import java.util.*;
public class inf2_2_7 {
    public String[] solution(String[] reports, int time){

        Map<String, Integer> hm = new HashMap<>();
        for(String r : reports){
            String nm = r.split(" ")[0];
            int t = Integer.parseInt(r.split(" ")[1].split(":")[0])*60 + Integer.parseInt(r.split(" ")[1].split(":")[1]);
            String op = r.split(" ")[2];

            if("in".equals(op)){
                hm.put(nm,hm.getOrDefault(nm,0)-t);
            }else{
                hm.put(nm,hm.getOrDefault(nm,0)+t);
            }
        }

        ArrayList<String> answerList = new ArrayList<>();
        for(Map.Entry<String, Integer> e : hm.entrySet()){
            /*System.out.println(e.getKey());
            System.out.println(e.getValue());*/

            if(e.getValue() > time){
                answerList.add(e.getKey());
            }
        }
        Collections.sort(answerList);
        String[] answer = new String[answerList.size()];
        int i=0;
        for(String s : answerList){
            answer[i] = s;
            i++;
        }
        return answer;
    }

    public static void main(String[] args){
        inf2_2_7 T = new inf2_2_7();
        System.out.println(Arrays.toString(T.solution(new String[]{"john 09:30 in", "daniel 10:05 in", "john 10:15 out", "luis 11:57 in", "john 12:03 in", "john 12:20 out", "luis 12:35 out", "daniel 15:05 out"}, 60)));
        System.out.println(Arrays.toString(T.solution(new String[]{"bill 09:30 in", "daniel 10:00 in", "bill 11:15 out", "luis 11:57 in", "john 12:03 in", "john 12:20 out", "luis 14:35 out", "daniel 14:55 out"}, 120)));
        System.out.println(Arrays.toString(T.solution(new String[]{"cody 09:14 in", "bill 09:25 in", "luis 09:40 in", "bill 10:30 out", "cody 10:35 out", "luis 10:35 out", "bill 11:15 in", "bill 11:22 out", "luis 15:30 in", "luis 15:33 out"}, 70)));
        System.out.println(Arrays.toString(T.solution(new String[]{"chato 09:15 in", "emilly 10:00 in", "chato 10:15 out", "luis 10:57 in", "daniel 12:00 in", "emilly 12:20 out", "luis 11:20 out", "daniel 15:05 out"}, 60)));
    }
}
