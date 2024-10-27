import java.util.*;
public class inf_1_7 {
    public static String solution(String str){
        String answer = "YES";

        int lt = 0;
        int rt = str.length()-1;
        str = str.toLowerCase();

        while(lt<rt){
            if(str.charAt(lt) != str.charAt(rt)){
                answer = "NO";
                break;
            }
            lt++;
            rt--;
        }
        return answer;
    }

    public static void main(String[] args){
        Scanner kb = new Scanner(System.in);
        String inp = kb.next();

        System.out.println(solution(inp));
    }
}
