import java.util.*;
public class inf_5_2 {
    public static String solution(String s){
        Stack<Character> stack = new Stack<>();
        int cnt = 0;
        for(char c:s.toCharArray()){
            if(c == '(') {
                cnt++;
            }else if(c == ')'){
                while(cnt > 0 && !stack.empty()){
                    if(stack.pop()=='('){
                        cnt--;
                        break;
                    }
                }
            }
            stack.push(c);
        }
        String answer = "";
        for(char c2:stack){
            if(c2 !='(' && c2 != ')')
                answer += Character.toString(c2);
        }
        return answer;
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
