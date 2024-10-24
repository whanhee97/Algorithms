import java.util.*;
public class inf_1_3 {
    public static String solution(String str){
        String answer = "";
        int cnt = 0;
        for(String x: str.split(" ")){
            if (x.length() > cnt){
                answer = x;
                cnt = x.length();
            }
        }
        return answer;
    }

    public static void main(String[] args){
        Scanner kb = new Scanner(System.in);
        String inp = kb.nextLine();

        System.out.println(solution(inp));
    }
}
