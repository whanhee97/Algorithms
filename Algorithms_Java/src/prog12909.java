import java.util.*;
public class prog12909 {
    boolean solution(String s) {
        boolean answer = true;
        Stack<Character> st = new Stack<>();

        for(char c:s.toCharArray()){
            if(c == ')' && !st.isEmpty()) st.pop();
            else st.push(c);
        }

        return st.isEmpty()?true:false;
    }
}
