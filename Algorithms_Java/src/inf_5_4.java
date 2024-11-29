import java.util.*;
public class inf_5_4 {
    public static int solution(String s){
        Stack<Integer> stack = new Stack<>();
        for(char c:s.toCharArray()){
            if(Character.isDigit(c)){
                stack.push(Character.getNumericValue(c));
            }else{
                int b = stack.pop();
                int a = stack.pop();
                switch(c){
                    case '+': stack.push(a+b);break;
                    case '-': stack.push(a-b);break;
                    case '*': stack.push(a*b);break;
                    case '/': stack.push(a/b);break;
                }
            }
        }
        return stack.peek();
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
