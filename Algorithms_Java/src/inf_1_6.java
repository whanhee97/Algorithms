import java.util.*;
public class inf_1_6 {
    public static String solution(String str){
        String answer = "";

        for(char c : str.toCharArray()){
            if(answer.indexOf(c) == -1)
                answer += c;
        }
        return answer;
    }

    public static void main(String[] args){
        Scanner kb = new Scanner(System.in);
        String inp = kb.next();

        System.out.println(solution(inp));
    }
}
