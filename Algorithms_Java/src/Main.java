//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
import java.util.*;

public class Main {
    /*public static void main(String[] args) {
        String input = "[[1, 4], [6, 3], [2, 5], [5, 1], [5, 3]]";
        input = input.replace("[","{");
        input = input.replace("]","}");
        System.out.print(input);
    }*/


    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[][] arr = new int[n][2];
        for(int i =0;i<n;i++){
            arr[i][0] = kb.nextInt();
            arr[i][1] = kb.nextInt();
        }

        inf_9_4 T = new inf_9_4();

        System.out.print(T.solution(n,arr));
    }
}