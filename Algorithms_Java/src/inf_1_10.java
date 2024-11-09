import java.util.*;
public class inf_1_10 {
    public static void setBoard(int[] b, int idx){
        for(int i=0;i<b.length;i++){
            int abs =  Math.abs(i-idx);
            if(b[i] > abs)
                b[i] = abs;
        }
    }

    public static int[] solution(String str, char target){
        int[] answer = new int[str.length()];
        for(int i = 0; i<str.length(); i++){
            answer[i] = 101;
        }
        for(int j = 0; j<str.length(); j++){
            if(str.charAt(j) == target){
                setBoard(answer,j);
            }
        }
        return answer;
    }

    public static void main(String[] args){
        Scanner kb = new Scanner(System.in);
        String s = kb.next();
        char t = kb.next().charAt(0);
        for(int x : solution(s,t)) {
            System.out.print(x+" ");
        }
    }
}
