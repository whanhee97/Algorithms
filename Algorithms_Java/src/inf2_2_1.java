import java.util.*;
public class inf2_2_1 {
    public int solution(String s){
        int answer = 0;
        Map<Character,Integer> m = new HashMap<>();
        for(char c : s.toCharArray()){
            m.put(c,m.getOrDefault(c,0)+1);
        }
        char key = ' ';
        boolean isExist = false;
        for(Map.Entry<Character, Integer> e : m.entrySet()){
            if(e.getValue() == 1){
                key = e.getKey();
                isExist = true;
                break;
            }
        }
        if(isExist){
            answer = s.indexOf(key) + 1;
        }else{
            answer = -1;
        }
        return answer;
    }

    public static void main(String[] args){
        inf2_2_1 T = new inf2_2_1();
        System.out.println(T.solution("statitsics"));
        System.out.println(T.solution("aabb"));
        System.out.println(T.solution("stringshowtime"));
        System.out.println(T.solution("abcdeabcdfg"));
    }
}
