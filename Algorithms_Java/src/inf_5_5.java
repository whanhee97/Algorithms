import java.util.*;
public class inf_5_5 {
    public static int solution(String s){
        int answer = 0;
        Stack<Character> st = new Stack<>();
        char pre = s.charAt(0);
        st.push(s.charAt(0));
        for(int i=1;i<s.length();i++){
            char c = s.charAt(i);
            if(c=='('){
                st.push(c);
            }else{
                st.pop();
                if(pre == '('){ // 레이저
                    answer += st.size();
                }else{
                    answer += 1;
                }
            }
            pre = c;
        }
        return answer;
    }

    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);

        String s = kb.next();


        System.out.println(solution(s));

    }
}

