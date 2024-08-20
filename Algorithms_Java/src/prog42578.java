import java.util.*;

public class prog42578 {
    public int Solution(String[][] clothes) {
        int answer = 0;
        int multi = 1;
        Map<String, ArrayList<String>> hm = new HashMap<>();
        for(String[] x:clothes){
            String key = x[1];
            String value = x[0];
            ArrayList<String> tmp = hm.getOrDefault(key,new ArrayList<String>());
            tmp.add(value);
            hm.put(key,tmp);
        }

        for(Map.Entry<String,ArrayList<String>> entry : hm.entrySet()){
            multi *= (entry.getValue().size()+1); // 각 의상 카테고리별 개수의 조합인데 안 입는 선택지도 있으므로 +1 해줌
        }
        answer = multi-1; // 아무것도 안 입는 경우 1건 빼줌

        return answer;
    }
    public static void main(String[] args) {
        prog42578 T = new prog42578();
        String[][] clothes = {{"e", "bs"}, {"f", "cm"}, {"f", "bb"}, {"f", "sm"}};
        System.out.print(T.Solution(clothes));
    }
}

