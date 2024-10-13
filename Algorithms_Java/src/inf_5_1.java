import java.util.*;
public class inf_5_1 {
    public static String solution(String s){
        if(s.charAt(s.length()-1) == '('){
            return "NO";
        }else{
            int cnt = 0;
            for(char c : s.toCharArray()){
                if(c == '('){
                    cnt++;
                }else{
                    cnt--;
                }
            }

            return cnt==0?"YES":"NO";
        }
    }

    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);

        String s = kb.next();


        System.out.println(solution(s));
        /*for(int x : solution(n,k,arr)){
            System.out.print(x + " ");
        }*/
    }
}
