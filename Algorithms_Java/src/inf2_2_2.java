import java.util.*;
public class inf2_2_2 {
    public int[] solution(String s){
        int[] answer = new int[5];
        Map<Character, Integer> m = new HashMap<>();
        m.put('a',0);
        m.put('b',0);
        m.put('c',0);
        m.put('d',0);
        m.put('e',0);
        for(char c : s.toCharArray()){
            m.put(c,m.getOrDefault(c,0)+1);
        }
        int max = 0;
        for(Map.Entry<Character, Integer> e : m.entrySet()){
            int val = e.getValue();
            if (val >= max){
                max = val;
            }
        }
        int idx = 0;
        for(Map.Entry<Character, Integer> e : m.entrySet()){
            int val = e.getValue();
            answer[idx] = max - val;
            idx++;

        }

        return answer;
    }

    public static void main(String[] args){
        inf2_2_2 T = new inf2_2_2();
        System.out.println(Arrays.toString(T.solution("aaabc")));
        System.out.println(Arrays.toString(T.solution("aabb")));
        System.out.println(Arrays.toString(T.solution("abcde")));
        System.out.println(Arrays.toString(T.solution("abcdeabc")));
        System.out.println(Arrays.toString(T.solution("abbccddee")));
    }
}
