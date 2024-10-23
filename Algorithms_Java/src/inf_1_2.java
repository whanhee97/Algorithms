import java.util.*;
public class inf_1_2 {
    public static String solution(String str){
        String answer = "";
        for(char x: str.toCharArray()){
            if(Character.isLowerCase(x)){
                answer += Character.toUpperCase(x);
            }else{
                answer += Character.toLowerCase(x);
            }
        }
        return answer;
    }

    public static void main(String[] args){
        Scanner kb = new Scanner(System.in);
        String inp = kb.next();

        System.out.println(solution(inp));
    }
}
