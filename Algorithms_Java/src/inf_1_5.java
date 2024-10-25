import java.util.*;
public class inf_1_5 {
    public static String solution(String str){

        char[] s = str.toCharArray();
        int lt = 0;
        int rt = str.length()-1;
        while(lt<rt){
            if(!Character.isAlphabetic(s[lt])){
                lt++;
                continue;
            }
            if(!Character.isAlphabetic(s[rt])){
                rt--;
                continue;
            }
            char tmp = s[lt];
            s[lt] = s[rt];
            s[rt] = tmp;
            lt++;
            rt--;
        }
        String answer = String.valueOf(s);

        return answer;
    }

    public static void main(String[] args){
        Scanner kb = new Scanner(System.in);
        String inp = kb.next();
        System.out.println(solution(inp));
    }
}
