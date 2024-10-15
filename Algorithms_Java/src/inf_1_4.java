import java.util.*;
public class inf_1_4 {
    public static String solution(String str){
        String answer = "";
        for (int j = str.toCharArray().length-1; j>=0; j--){
            answer += str.charAt(j);
        }
        return answer;
    }

    public static void main(String[] args){
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        for(int i=0;i<n;i++){
            System.out.println(solution(kb.next()));
        }
    }
}
