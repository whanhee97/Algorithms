import java.util.*;
public class inf_1_9 {
    public static int solution(String str){
        int answer;

        String sNum = str.replaceAll("[A-Za-z]","");
        answer = Integer.parseInt(sNum);
        return answer;
    }

    public static void main(String[] args){
        Scanner kb = new Scanner(System.in);
        String inp = kb.nextLine();

        System.out.println(solution(inp));
    }
}
