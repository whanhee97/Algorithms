import java.util.*;
public class inf2_2_3 {
    public int solution(String s){
        int answer = 0;
        Map<Character, Integer> m = new HashMap<>();
        for(char c : s.toCharArray()){
            m.put(c, m.getOrDefault(c,0)+1);
        }
        int size = m.values().size();
        Integer[] values = m.values().toArray(new Integer[size]);

        for(int i=0;i<size;i++){
            Integer tmp = values[i];
            for(int j=i+1;j<size;j++){
                if(tmp == values[j] && tmp != 0){
                    values[j]--;
                    answer++;
                }
            }
        }
        return answer;
    }

    public static void main(String[] args){
        inf2_2_3 T = new inf2_2_3();
        System.out.println(T.solution("aaabbbcc"));
        System.out.println(T.solution("aaabbc"));
        System.out.println(T.solution("aebbbbc"));
        System.out.println(T.solution("aaabbbcccde"));
        System.out.println(T.solution("aaabbbcccdddeeeeeff"));
    }
}
