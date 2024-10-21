import java.util.*;
public class inf_1_1 {
    public static int solution(String ip1, char ip2){
        ip1 = ip1.toUpperCase();
        ip2 = Character.toUpperCase(ip2);

        int cnt = 0;
        for (char c : ip1.toCharArray()) {
            if (c == ip2) {
                cnt++;
            }
        }
        return cnt;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner in = new Scanner(System.in);
        String input1 = in.next();
        char input2 = in.next().charAt(0);

        System.out.println(solution(input1,input2));
    }
}
