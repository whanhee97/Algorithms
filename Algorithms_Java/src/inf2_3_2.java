import java.util.*;
public class inf2_3_2 {
    public String solution(String s){
        String answer = "";
        Stack<String> st = new Stack<>();
        for(char c : s.toCharArray()){ // 하나씩 읽어서
            if(c != ')'){ // 닫는 괄호 아니면 그냥 스택에 넣어주고
                st.push(String.valueOf(c));
            }else{ // 닫는 괄호면
                int cnt = 1;
                String tmp = "";
                while(!st.isEmpty()){
                    String now = st.pop();
                    if(Character.isDigit(now.charAt(0)) ){ // 스택에서 뽑은게 숫자면
                        cnt = Integer.parseInt(now);
                        break; // 숫자 저장하고 멈춤
                    }else{ // 숫자가 아니면
                        if(!"(".equals(now)){
                            tmp = now + tmp; // ( 제외하고 역순으로 문자열 저장함
                        }
                    }
                }

                String tmp2 = "";
                for(int i=0;i<cnt;i++){
                    tmp2 += tmp; // 만들어진 문자열을 cnt 만큼 곱해줌
                }

                st.push(tmp2); // 다시 스택에 추가
            }
        }
        while(!st.isEmpty()){
            answer = st.pop() + answer;
        }
        return answer;
    }

    public static void main(String[] args){
        inf2_3_2 T = new inf2_3_2();
        System.out.println(T.solution("3(a2(b))ef"));
        System.out.println(T.solution("2(ab)k3(bc)"));
        System.out.println(T.solution("2(ab3((cd)))"));
        System.out.println(T.solution("2(2(ab)3(2(ac)))"));
        System.out.println(T.solution("3(ab2(sg))"));
    }
}
