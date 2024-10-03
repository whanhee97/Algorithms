import java.util.HashMap;
import java.util.Scanner;

public class inf_4_2 {
    public static String solution(String str1,String str2){
        HashMap<Character,Integer> map = new HashMap<>();
        HashMap<Character,Integer> map2 = new HashMap<>();
        for(char c : str1.toCharArray()){
            map.put(c,map.getOrDefault(c,0)+1);
        }
        for(char c : str2.toCharArray()){
            map2.put(c,map2.getOrDefault(c,0)+1);
        }
        String answer;
        answer=map.entrySet().equals(map2.entrySet())?"YES":"NO";
        return answer;
    }

    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);

        String s1 = kb.next();
        String s2 = kb.next();
        System.out.println(solution(s1,s2));
    }
}


